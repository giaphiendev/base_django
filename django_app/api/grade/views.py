import datetime

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.grade.serializers import PostGradeSerializer, GetGradeSerializer, GetClassSubjectSerializer
from core.decorators import map_exceptions
from core.models import UserType, User
from custom_service.errors import ERROR_STUDENT_NOT_FOUND
from custom_service.exceptions import StudentNotFound
from custom_service.handlers.grade import GradeHandle
from custom_service.models.ModelTechwiz import ClassTeacherSubject, Student
from custom_service.task import send_notification_to_device_celery


class GetGradeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        '''
        get subject
        arg:
        '''
        term = request.GET.get('term')
        if term is None:
            return Response({"payload": []}, status=200)
        role = request.user.role
        if role is None:
            return Response({"payload": []}, status=200)

        elif role == UserType.STUDENT:
            student_id = Student.objects.filter(user_id=request.user.id).first().id
            data_res = GradeHandle().get_grade_family(student_id, term)
            return Response({"payload": data_res}, status=200)
        elif role == UserType.PARENT:
            student_id = request.GET.get('student_id')
            data_res = GradeHandle().get_grade_family(student_id, term)
            return Response({"payload": data_res}, status=200)
        return Response({"payload": []}, status=200)


class GetSubjectView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        '''
        get subject
        arg:
        '''
        role = request.user.role
        if role is None:
            return Response({"payload": []}, status=200)

        if role == UserType.TEACHER:
            list_subject = ClassTeacherSubject.objects.filter(teacher_id=request.user.id).select_related(
                'subject').values_list('subject_id', 'subject__name').all()
            data = []
            for item in list(set(list_subject)):
                data.append({
                    "id": item[0],
                    "name": item[1],
                })
            return Response({"payload": data}, status=200)
        elif role == UserType.STUDENT:
            student = Student.objects.filter(user=request.user).select_related('my_class').first()
            list_subject = ClassTeacherSubject.objects.filter(my_class_id=student.my_class_id).select_related(
                'subject').values_list('subject_id', 'subject__name').all()
            data = []
            for item in list(set(list_subject)):
                data.append({
                    "id": item[0],
                    "name": item[1],
                })
            return Response({"payload": data}, status=200)

        return Response({"payload": []}, status=200)


class GetInputGradeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        '''
        get input grade,
        only teacher has permission
        arg:
        '''
        role = request.user.role
        if role is None or role != UserType.TEACHER:
            return Response({"payload": []}, status=200)

        # data_res = GradeHandle().get_input_grade(request.user.id)
        data_res = GradeHandle().recent_grade(request.user.id)
        return Response({"payload": data_res}, status=200)


class GetClassSubjectView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetClassSubjectSerializer

    def get(self, request):
        '''
        get all grade of class
        arg:
            teacher_id
        '''
        role = request.user.role
        if role is None:
            return Response({"payload": []}, status=200)
        if role == UserType.TEACHER:
            list_class_subject = ClassTeacherSubject.objects.filter(
                teacher_id=request.user.id
            ).select_related('my_class', 'subject').all()
            serializer = self.serializer_class(list_class_subject, many=True, context=role).data
            data = {
                'payload': serializer
            }
            return Response(data, status=200)

        elif role == UserType.STUDENT:
            student = Student.objects.filter(user_id=request.user.id).first()
            if student is None:
                return Response({"payload": []}, status=200)
            list_class_subject = ClassTeacherSubject.objects.filter(
                my_class_id=student.my_class.id
            ).select_related('my_class', 'subject').all()

            serializer = self.serializer_class(list_class_subject, many=True, context=role).data
            data = {
                'payload': serializer
            }
            return Response(data, status=200)

        return Response({"payload": []}, status=200)


class CreateGradeView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PostGradeSerializer

    def get(self, request):
        '''
        get all grade of class for each role (student, )
        nam hoc tinh tu 1/9 => 30/8
        arg:
            subject_id
            class_id
            term
        '''
        subject_id = request.GET.get('subject_id', None)
        class_id = request.GET.get('class_id', None)
        term = request.GET.get('term', None)
        if subject_id is None or class_id is None or term is None:
            return Response({"payload": []}, status=200)

        grades = GradeHandle().list_of_grade_by_class({
            "term": term,
            "class_id": class_id,
            "subject_id": subject_id
        })
        data = {
            'payload': grades
        }
        return Response(data, status=200)

    @map_exceptions(
        {
            StudentNotFound: ERROR_STUDENT_NOT_FOUND,
        }
    )
    # @validate_body(PostGradeSerializer)
    def post(self, request):
        data = request.data
        data['teacher_id'] = request.user.id
        role = request.user.role
        if role != UserType.TEACHER:
            return Response({'payload': "You have no permission"}, status=400)
        if data.get('grade_id') is None:
            grade = GradeHandle().add_grade(data)

        else:
            grade = GradeHandle().update_grade(data)

        serializer = GetGradeSerializer(grade).data

        # push_notification change mark
        student_id = grade.student.id

        student = Student.objects.filter(id=student_id).first()
        user_id = student.user_id
        parent_id = student.parent_id

        term = 1 if grade.term == "TERM1" else 2

        data_push_notification = {
            "title": f"Teacher {request.user.first_name} {request.user.last_name}",
            "message": f"Grade update for {student.user.first_name} {student.user.last_name} {grade.subject.name} term {term} {grade.type_exam} | 2021 - 2022",
            "extra": {"created_at": datetime.datetime.now().date()},
            "user_id": [user_id, parent_id]
        }
        send_notification_to_device_celery.delay(data_push_notification)

        data = {
            'payload': serializer
        }

        return Response(data, status=200)
#
#
# class GetListPostView(PaginationApiView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         all_post = Post.objects.all()
#         page_info, paginated_data = self.get_paginated(all_post)
#         post_serializer = PostSerializer(paginated_data, many=True).data
#         data = {
#             'data': post_serializer,
#             'page_info': page_info
#         }
#         return Response(data, status=200)
#
#     @validate_body(PutPostSerializer)
#     def post(self, request, data):
#         post = PostHandler().create_post(data)
#         post_serializer = PostSerializer(post).data
#         data = {
#             'data': post_serializer
#         }
#         return Response(data, status=200)
#
#
# class DetailPostView(APIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = PostSerializer
#     handler_class = PostHandler
#
#     @map_exceptions(
#         {
#             PostNotFound: ERROR_POST_NOT_FOUND,
#         }
#     )
#     def get(self, request, post_id):
#         post = self.handler_class().get_post(post_id)
#         post_serializer = self.serializer_class(post).data
#         data = {
#             'data': post_serializer
#         }
#         return Response(data, status=200)
#
#     @map_exceptions(
#         {
#             PostNotFound: ERROR_POST_NOT_FOUND,
#         }
#     )
#     @validate_body(PutPostSerializer)
#     def put(self, request, post_id, data):
#         post = self.handler_class().update_post(post_id, data)
#         post_serializer = self.serializer_class(post).data
#         data_res = {
#             'data': post_serializer
#         }
#         return Response(data_res, status=200)
#
#     @map_exceptions(
#         {
#             PostNotFound: ERROR_POST_NOT_FOUND,
#         }
#     )
#     def delete(self, request, **kwargs):
#         post_id = kwargs.get("post_id")
#         self.handler_class().delete_post(post_id)
#         data = {
#             'payload': None,
#             'error': None
#         }
#         return Response(data, status=204)
