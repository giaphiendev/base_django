from django.db import transaction

from custom_service.exceptions import PostNotFound
from custom_service.models.ModelTechwiz import HelpLine


class Handler:
    def get_helplines(self, pk):
        """
        Get helplines by id
        """
        try:
            return HelpLine.objects.get(
                pk=pk,
            )
        except HelpLine.DoesNotExist:
            raise PostNotFound(f"The Class not found")

    def create_helplines(self, data):
        """
        Create helplines
        """
        with transaction.atomic():
            helplines = HelpLine.objects.create(**data)

        return helplines

    def update_helplines(self, pk, data):
        """
        Update helplines
        """
        with transaction.atomic():
            HelpLine.objects.filter(pk=pk).update(**data)
            # Update cart
            return self.get_helplines(pk)

    def delete_helplines(self, pk):
        """
        Delete a helplines
        """
        post = self.get_helplines(pk)
        post.delete()
