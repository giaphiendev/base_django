from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.helplines.serializers import HelpLineSerializer, PutHelpLineSerializer
from core.decorators import map_exceptions, validate_body
from custom_service.errors import ERROR_POST_NOT_FOUND
from custom_service.exceptions import PostNotFound
from custom_service.models.ModelTechwiz import HelpLine
from utils.base_views import PaginationApiView


class GetListHelpLinesView(PaginationApiView):
    permission_classes = (IsAuthenticated,)  # IsAuthenticated

    def get(self, request):
        all_helplines = HelpLine.objects.all()
        page_info, paginated_data = self.get_paginated(all_helplines)
        helplines_serializer = HelpLineSerializer(paginated_data, many=True).data
        data = {
            'data': helplines_serializer,
            'page_info': page_info
        }
        return Response(data, status=200)

    # @validate_body(PutHelpLineSerializer)
    # def post(self, request, data):
    #     helpline = MyClassHandler().create_myClass(data)
    #     myClass_serializer = MyClassSerializer(myClass).data
    #     data = {
    #         'data': myClass_serializer
    #     }
    #     return Response(data, status=200)

#
# class DetailMyClassView(APIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = MyClassSerializer
#     handler_class = MyClassHandler
#
#     @map_exceptions(
#         {
#             PostNotFound: ERROR_POST_NOT_FOUND,
#         }
#     )
#     def get(self, request, class_id):
#         myClass = self.handler_class().get_myClass(class_id)
#         myClass_serializer = self.serializer_class(myClass).data
#         data = {
#             'data': myClass_serializer
#         }
#         return Response(data, status=200)
#
#     @map_exceptions(
#         {
#             PostNotFound: ERROR_POST_NOT_FOUND,
#         }
#     )
#     @validate_body(PutMyClassSerializer)
#     def put(self, request, class_id, data):
#         myClass = self.handler_class().update_post(class_id, data)
#         myClass_serializer = self.serializer_class(myClass).data
#         data_res = {
#             'data': myClass_serializer
#         }
#         return Response(data_res, status=200)
#
#     @map_exceptions(
#         {
#             PostNotFound: ERROR_POST_NOT_FOUND,
#         }
#     )
#     def delete(self, request, **kwargs):
#         class_id = kwargs.get("class_id")
#         self.handler_class().delete_myClass(class_id)
#         data = {
#             'payload': None,
#             'error': None
#         }
#         return Response(data, status=204)
