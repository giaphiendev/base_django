# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from api.post.serializers import PostSerializer, PutPostSerializer
# from core.decorators import map_exceptions, validate_body
# from custom_service.errors import ERROR_POST_NOT_FOUND
# from custom_service.exceptions import PostNotFound
# from custom_service.handlers.demo import PostHandler
# from custom_service.models.demo import Post
# from utils.base_views import PaginationApiView
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
