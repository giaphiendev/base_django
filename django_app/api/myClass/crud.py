from django.db import transaction

from custom_service.exceptions import PostNotFound
from custom_service.models.ModelTechwiz import MyClass


class MyClassHandler:
    def get_myClass(self, pk):
        """
        Get myClass by id
        """
        try:
            return MyClass.objects.get(
                pk=pk,
            )
        except MyClass.DoesNotExist:
            raise PostNotFound(f"The Class not found")

    def create_myClass(self, data):
        """
        Create Class
        """
        with transaction.atomic():
            myclass = MyClass.objects.create(**data)

        return myclass

    def update_myClass(self, pk, data):
        """
        Update Class
        """
        with transaction.atomic():
            MyClass.objects.filter(pk=pk).update(**data)
            # Update cart
            return self.get_myClass(pk)

    def delete_myClass(self, pk):
        """
        Delete a class
        """
        post = self.get_myClass(pk)
        post.delete()
