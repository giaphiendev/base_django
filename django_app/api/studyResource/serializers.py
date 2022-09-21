from rest_framework import serializers

from custom_service.models.ModelTechwiz import StudyResource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyResource
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
        }


class PutResourceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=255)
    link = serializers.CharField(max_length=255)
    subject = serializers.IntegerField()
    
