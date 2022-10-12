from django.db import transaction

from custom_service.exceptions import PostNotFound
from custom_service.models.ModelTechwiz import ClassTeacherSubject


class Handler:
    def get(self, pk):

        try:
            return ClassTeacherSubject.objects.get(
                pk=pk,
            )
        except ClassTeacherSubject.DoesNotExist:
            raise PostNotFound(f"The class teacher subject not found")

    def create(self, data):

        with transaction.atomic():
            temp = ClassTeacherSubject.objects.create(**data)

        return temp

    def update(self, pk, data):

        with transaction.atomic():
            ClassTeacherSubject.objects.filter(pk=pk).update(**data)
            return self.get(pk)

    def delete(self, pk):
        """
        Delete subject
        """
        post = self.get(pk)
        post.delete()
