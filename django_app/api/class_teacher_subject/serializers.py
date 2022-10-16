from rest_framework import serializers

from api.myClass.serializers import MyClassSerializer
from api.subject.serializers import SubjectSerializer
from api.user.serializers import GetUserSerializer
from core.models import User
from custom_service.models.ModelTechwiz import ClassTeacherSubject, MyClass, Subject


class ClassTeacherSubjectSerializer(serializers.Serializer):
    info = serializers.SerializerMethodField()

    def get_info(self, instance):
        return {
            **instance
        }


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
