from rest_framework import serializers

from custom_service.models.ModelTechwiz import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
        }


class PutSubjectSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
