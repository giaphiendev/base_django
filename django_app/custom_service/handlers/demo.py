from django.db import transaction

from custom_service.exceptions import PostNotFound
from custom_service.models.demo import Post


class PostHandler:
    def get_post(self, pk):
        """
        Get post by id
        """
        try:
            return Post.objects.get(
                pk=pk,
            )
        except Post.DoesNotExist:
            raise PostNotFound(f"The post not found")

    def create_post(self, data):
        """
        Create post
        """
        with transaction.atomic():
            post = Post.objects.create(**data)

        return post

    def update_post(self, pk, data):
        """
        Update post
        """
        with transaction.atomic():
            Post.objects.filter(pk=pk).update(**data)
            # Update cart
            return self.get_post(pk)

    def delete_post(self, pk):
        """
        Delete a post
        """
        post = self.get_post(pk)
        post.delete()
