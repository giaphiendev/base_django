from datetime import datetime

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from api.studyResource.serializers import ResourceSerializer, PutResourceSerializer, GetResourceSerializer
from core.decorators import map_exceptions, validate_body
from core.models import UserType
from custom_service.errors import ERROR_POST_NOT_FOUND
from custom_service.exceptions import PostNotFound
from .crud import StudyResourceHandler
from custom_service.models.ModelTechwiz import StudyResource, Subject, Student, ClassTeacherSubject
from utils.base_views import PaginationApiView
from custom_service.task import send_notification_to_device_celery


class GetResource(PaginationApiView):
    permission_classes = (AllowAny,)

    def get(self, request):
        subject_id = request.GET.get('subject_id', None)
        if subject_id is None:
            all_resource = StudyResource.objects.all()
        else:
            all_resource = StudyResource.objects.filter(subject_id=subject_id).select_related('subject').all()
        page_info, paginated_data = self.get_paginated(all_resource)
        post_serializer = GetResourceSerializer(paginated_data, many=True).data
        payload = []
        if len(post_serializer):
            for item in post_serializer:
                payload.append({**item.get('info')})
        data = {
            'data': payload,
            'page_info': page_info
        }
        return Response(data, status=200)

    # @validate_body(PutResourceSerializer)
    def post(self, request):
        role = request.user.role
        if role != UserType.TEACHER:
            return Response({'payload': "You have no permission!"}, status=200)
        data = request.data
        subject = Subject.objects.filter(id=data.get('subject')).first()
        data["subject"] = subject
        resource = StudyResourceHandler().create_resource(data)
        resource_serializer = ResourceSerializer(resource).data

        # push_notification add resource
        class_teacher_subject = ClassTeacherSubject.objects.filter(
            subject_id=data.get('subject'),
            teacher_id=request.user.id
        ).values_list('my_class_id', flat=True)

        user_id = Student.objects.filter(
            my_class_id__in=class_teacher_subject
        ).select_related('user').values_list('user_id', flat=True)

        data_push_notification = {
            "title": f"Teacher {request.user.first_name} {request.user.last_name} \n {resource.name}",
            "message": f"A new study resource has been added for {subject.name} | 2021 - 2022",
            "extra": {"created_at": datetime.now()},
            "user_id": list(set(user_id))
        }
        send_notification_to_device_celery.delay(data_push_notification)

        data = {
            'data': resource_serializer
        }
        return Response(data, status=200)


class DetailResourceView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ResourceSerializer
    handler_class = StudyResourceHandler

    @map_exceptions(
        {
            PostNotFound: ERROR_POST_NOT_FOUND,
        }
    )
    def get(self, request, resource_id):
        resource = self.handler_class().get_resource(resource_id)
        resource_serializer = self.serializer_class(resource).data
        data = {
            'data': resource_serializer
        }
        return Response(data, status=200)

    @map_exceptions(
        {
            PostNotFound: ERROR_POST_NOT_FOUND,
        }
    )
    @validate_body(PutResourceSerializer)
    def put(self, request, resource_id, data):
        resource = self.handler_class().update_resource(resource_id, data)
        resource_serializer = self.serializer_class(resource).data
        data_res = {
            'data': resource_serializer
        }
        return Response(data_res, status=200)

    @map_exceptions(
        {
            PostNotFound: ERROR_POST_NOT_FOUND,
        }
    )
    def delete(self, request, **kwargs):
        resource_id = kwargs.get("resource_id")
        self.handler_class().delete_resource(resource_id)
        data = {
            'payload': None,
            'error': None
        }
        return Response(data, status=204)


class CreateView(PaginationApiView):
    permission_classes = (AllowAny,)  # IsAuthenticated

    # def get(self, request):
    #     all_helplines = HelpLine.objects.all()
    #     page_info, paginated_data = self.get_paginated(all_helplines)
    #     helplines_serializer = HelpLineSerializer(paginated_data, many=True).data
    #     data = {
    #         'data': helplines_serializer,
    #         'page_info': page_info
    #     }
    #     return Response(data, status=200)

    @validate_body(PutResourceSerializer)
    def post(self, request, data):
        # data = request.data
        data["subject"] = Subject.objects.filter(id=data.get('subject')).first()
        resource = StudyResourceHandler().create_resource(data)
        serializer = ResourceSerializer(resource).data
        data = {
            'data': serializer
        }
        return Response(data, status=200)
