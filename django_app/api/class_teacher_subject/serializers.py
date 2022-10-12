from rest_framework import serializers

from custom_service.models.ModelTechwiz import ClassTeacherSubject


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = ClassTeacherSubject
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
        }


class PutSerializer(serializers.Serializer):
    my_class = serializers.IntegerField()
    subject = serializers.IntegerField()
    teacher = serializers.IntegerField()
