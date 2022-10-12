from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.subject.serializers import SubjectSerializer, PutSubjectSerializer
from core.decorators import map_exceptions, validate_body
from custom_service.errors import ERROR_POST_NOT_FOUND
from custom_service.exceptions import PostNotFound
from .crud import SubjectHandler
from custom_service.models.ModelTechwiz import Subject
from utils.base_views import PaginationApiView


class GetListSubjectView(PaginationApiView):
    permission_classes = (AllowAny,)

    def get(self, request):
        all_post = Subject.objects.all()
        page_info, paginated_data = self.get_paginated(all_post)
        post_serializer = SubjectSerializer(paginated_data, many=True).data
        data = {
            'data': post_serializer,
            'page_info': page_info
        }
        return Response(data, status=200)

    @validate_body(PutSubjectSerializer)
    def post(self, request, data):
        subject = SubjectHandler().create_subject(data)
        subject_serializer = SubjectSerializer(subject).data
        data = {
            'data': subject_serializer
        }
        return Response(data, status=200)


class DetailSubjectView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = SubjectSerializer
    handler_class = SubjectHandler

    @map_exceptions(
        {
            PostNotFound: ERROR_POST_NOT_FOUND,
        }
    )
    def get(self, request, subject_id):
        subject = self.handler_class().get_subject(subject_id)
        subject_serializer = self.serializer_class(subject).data
        data = {
            'data': subject_serializer
        }
        return Response(data, status=200)

    @map_exceptions(
        {
            PostNotFound: ERROR_POST_NOT_FOUND,
        }
    )

    def delete(self, request, **kwargs):
        subject_id = kwargs.get("subject_id")
        self.handler_class().delete_subject(subject_id)
        data = {
            'payload': None,
            'error': None
        }
        return Response(data, status=204)

    def put(self, request, subject_id):
        data = request.data
        subject = SubjectHandler().update_subject(subject_id, data)
        serializer = SubjectSerializer(subject).data
        data = {
            'payload': serializer
        }
        return Response(data, status=200)
