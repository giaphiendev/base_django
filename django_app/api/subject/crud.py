from django.db import transaction

from custom_service.exceptions import PostNotFound
from custom_service.models.ModelTechwiz import Subject


class SubjectHandler:
    def get_subject(self, pk):
        """
        Get subject by id
        """
        try:
            return Subject.objects.get(
                pk=pk,
            )
        except Subject.DoesNotExist:
            raise PostNotFound(f"The subject not found")

    def create_subject(self, data):
        """
        Create subject
        """
        with transaction.atomic():
            resource = Subject.objects.create(**data)

        return resource

    def update_subject(self, pk, data):
        """
        Update subject
        """
        with transaction.atomic():
            Subject.objects.filter(pk=pk).update(**data)
            return self.get_subject(pk)

    def delete_subject(self, pk):
        """
        Delete subject
        """
        post = self.get_subject(pk)
        post.delete()
