from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.grade.serializers import PostGradeSerializer
from core.decorators import validate_body, map_exceptions
from custom_service.errors import ERROR_STUDENT_NOT_FOUND, ERROR_GRADE_NOT_FOUND
from custom_service.exceptions import StudentNotFound, ExamNotFound
from custom_service.handlers.grade import GradeHandle


class CreateGradeView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostGradeSerializer

    def get(self, request):
        data = {
            'payload': None
        }
        return Response(data, status=200)

    @map_exceptions(
        {
            StudentNotFound: ERROR_STUDENT_NOT_FOUND,
            ExamNotFound: ERROR_GRADE_NOT_FOUND,
        }
    )
    @validate_body(PostGradeSerializer)
    def post(self, request, data):
        GradeHandle().add_grade(data)
        data = {
            'payload': None
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
