from rest_framework import serializers

from custom_service.models.ModelTechwiz import Student

#
# class GetStudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = "__all__"
#         extra_kwargs = {
#             "id": {"read_only": True},
#         }
