from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.helplines.serializers import HelpLineSerializer, PutHelpLineSerializer
from core.decorators import map_exceptions, validate_body
from custom_service.errors import ERROR_POST_NOT_FOUND
from custom_service.exceptions import PostNotFound
from custom_service.models.ModelTechwiz import HelpLine
from utils.base_views import PaginationApiView
from api.helplines.crud import Handler


class GetListHelpLinesView(PaginationApiView):
    permission_classes = (AllowAny,)  # IsAuthenticated

    def get(self, request):
        all_helplines = HelpLine.objects.all()
        page_info, paginated_data = self.get_paginated(all_helplines)
        helplines_serializer = HelpLineSerializer(paginated_data, many=True).data
        data = {
            'data': helplines_serializer,
            'page_info': page_info
        }
        return Response(data, status=200)

    @validate_body(PutHelpLineSerializer)
    def post(self, request, data):
        helplines = Handler().create_helplines(data)
        serializer = HelpLineSerializer(helplines).data
        data = {
            'data': serializer
        }
        return Response(data, status=200)

class DetailView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = HelpLineSerializer
    handler_class = Handler
    @map_exceptions(
        {
            PostNotFound: ERROR_POST_NOT_FOUND,
        }
    )
    def get(self, request, helplines_id):
        helplines = self.handler_class().get_helplines(helplines_id)
        serializer = self.serializer_class(helplines).data
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
        helplines_id = kwargs.get("helplines_id")
        self.handler_class().delete_helplines(helplines_id)
        return Response(
                {
                    'payload': None
                },
                status=204
            )
    def put(self, request, helplines_id):
        data = request.data
        helplines = Handler().update_helplines(helplines_id, data)
        serializer = HelpLineSerializer(helplines).data
        data = {
            'payload': serializer
        }
        return Response(data, status=200)

