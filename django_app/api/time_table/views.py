from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import Serializer, PutSerializer
from core.decorators import map_exceptions, validate_body
from custom_service.errors import ERROR_POST_NOT_FOUND
from custom_service.exceptions import PostNotFound
from .crud import Handler
from custom_service.models.ModelTechwiz import TimeTable, RevisionClass
from utils.base_views import PaginationApiView


class GetListView(PaginationApiView):
    permission_classes = (AllowAny,)  # IsAuthenticated

    def get(self, request, revision_id):
        """

            get time table by revision id

        """
        all = TimeTable.objects.filter(revision_class_id=revision_id).all()
        page_info, paginated_data = self.get_paginated(all)
        serializer = Serializer(paginated_data, many=True).data
        data = {
            'data': serializer,
            'page_info': page_info
        }
        return Response(data, status=200)

    @validate_body(PutSerializer)
    def post(self, request, data):
        temp = Handler().create(data)
        serializer = Serializer(temp).data
        data = {
            'data': serializer
        }
        return Response(data, status=200)

class DetailView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = Serializer
    handler_class = Handler
    @map_exceptions(
        {
            PostNotFound: ERROR_POST_NOT_FOUND,
        }
    )
    def get(self, request, id):
        temp = self.handler_class().get(id)
        serializer = self.serializer_class(temp).data
        data = {
            'data': serializer
        }
        return Response(data, status=200)

    @map_exceptions(
        {
            PostNotFound: ERROR_POST_NOT_FOUND,
        }
    )
    def delete(self, request, **kwargs):
        id = kwargs.get("id")
        self.handler_class().delete(id)
        return Response(
                {
                    'payload': None
                },
                status=204
            )
    def put(self, request, id):
        data = request.data
        temp = Handler().update(id, data)
        serializer = Serializer(temp).data
        data = {
            'payload': serializer
        }
        return Response(data, status=200)

