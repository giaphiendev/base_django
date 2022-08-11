from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.grade.serializers import PostGradeSerializer, GetGradeSerializer, GetClassSubjectSerializer
from core.decorators import validate_body, map_exceptions
from custom_service.errors import ERROR_STUDENT_NOT_FOUND, ERROR_GRADE_NOT_FOUND
from custom_service.exceptions import StudentNotFound
from custom_service.handlers.grade import GradeHandle
from custom_service.models.ModelTechwiz import ClassTeacherSubject


class GetClassSubjectView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetClassSubjectSerializer

    def get(self, request):
        '''
        get all grade of class
        arg:
            teacher_id
        '''
        teacher_id = request.GET.get('teacher_id', None)
        if teacher_id is None:
            return Response({"payload": []}, status=200)
        list_class_subject = ClassTeacherSubject.objects.filter(teacher_id=teacher_id).select_related('my_class',
                                                                                                      'subject').all()
        serializer = self.serializer_class(list_class_subject, many=True).data
        data = {
            'payload': serializer
        }
        return Response(data, status=200)


class CreateGradeView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostGradeSerializer

    def get(self, request):
        '''
        get all grade of class
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
    @validate_body(PostGradeSerializer)
    def post(self, request, data):
        grade = GradeHandle().add_grade(data)
        serializer = GetGradeSerializer(grade).data
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
