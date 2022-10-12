from django.db import transaction

from custom_service.exceptions import PostNotFound
from custom_service.models.ModelTechwiz import TimeTable


class Handler:
    def get(self, pk):

        try:
            return TimeTable.objects.get(
                pk=pk,
            )
        except TimeTable.DoesNotExist:
            raise PostNotFound(f"Time table not found")

    def create(self, data):

        with transaction.atomic():
            temp = TimeTable.objects.create(**data)

        return temp

    def update(self, pk, data):

        with transaction.atomic():
            TimeTable.objects.filter(pk=pk).update(**data)
            return self.get(pk)

    def delete(self, pk):
        """
        Delete subject
        """
        post = self.get(pk)
        post.delete()
