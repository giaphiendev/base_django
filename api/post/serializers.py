# from rest_framework import serializers
#
# from custom_service.models.demo import Post
#
#
# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = "__all__"
#         extra_kwargs = {
#             "id": {"read_only": True},
#         }
#
#
# class PutPostSerializer(serializers.Serializer):
#     title = serializers.CharField(required=True, max_length=255)
#     description = serializers.CharField(required=False)
