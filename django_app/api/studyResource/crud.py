from django.db import transaction

from custom_service.exceptions import PostNotFound
from custom_service.models.ModelTechwiz import StudyResource


class StudyResourceHandler:
    def get_resource(self, pk):
        """
        Get study resource by id
        """
        try:
            return StudyResource.objects.get(
                pk=pk,
            )
        except StudyResource.DoesNotExist:
            raise PostNotFound(f"The Class not found")

    def create_resource(self, data):
        """
        Create study resource
        """
        with transaction.atomic():
            resource = StudyResource.objects.create(**data)

        return resource

    def update_resource(self, pk, data):
        """
        Update study resource
        """
        with transaction.atomic():
            StudyResource.objects.filter(pk=pk).update(**data)
            # Update cart
            return self.get_resource(pk)

    def delete_resource(self, pk):
        """
        Delete a study resource
        """
        post = self.get_resource(pk)
        post.delete()
