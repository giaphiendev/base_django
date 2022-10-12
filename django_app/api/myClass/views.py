from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.myClass.serializers import MyClassSerializer, PutMyClassSerializer
from core.decorators import map_exceptions, validate_body
from custom_service.errors import ERROR_POST_NOT_FOUND
from custom_service.exceptions import PostNotFound
from .crud import MyClassHandler
from custom_service.models.ModelTechwiz import MyClass
from utils.base_views import PaginationApiView


class GetListMyClassView(PaginationApiView):
    permission_classes = (AllowAny,)

    def get(self, request):
        all_post = MyClass.objects.all()
        page_info, paginated_data = self.get_paginated(all_post)
        post_serializer = MyClassSerializer(paginated_data, many=True).data
        data = {
            'data': post_serializer,
            'page_info': page_info
        }
        return Response(data, status=200)

    @validate_body(PutMyClassSerializer)
    def post(self, request, data):
        myClass = MyClassHandler().create_myClass(data)
        myClass_serializer = MyClassSerializer(myClass).data
        data = {
            'data': myClass_serializer
        }
        return Response(data, status=200)


class DetailMyClassView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = MyClassSerializer
    handler_class = MyClassHandler

    @map_exceptions(
        {
            PostNotFound: ERROR_POST_NOT_FOUND,
        }
    )

    def get(self, request, myClass_id):
        myclass = self.handler_class().get_myClass(myClass_id)
        serializer = self.serializer_class(myclass).data
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
        myClass_id = kwargs.get("myClass_id")
        self.handler_class().delete_myClass(myClass_id)
        return Response(
                {
                    'payload': None
                },
                status=204
            )
    def put(self, request, myClass_id):
        data = request.data
        myclass = MyClassHandler().update_myClass(myClass_id, data)
        serializer = MyClassSerializer(myclass).data
        data = {
            'payload': serializer
        }
        return Response(data, status=200)
