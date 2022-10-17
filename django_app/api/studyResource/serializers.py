from rest_framework import serializers

from custom_service.models.ModelTechwiz import StudyResource


class GetResourceSerializer(serializers.Serializer):
    info = serializers.SerializerMethodField()

    def get_info(self, instance):
        name = instance.name
        type = instance.type
        link = instance.link
        subject_name = instance.subject.id
        subject_id = instance.subject.name
        return {
            "name": name,
            "type": type,
            "link": link,
            "subject_name": subject_name,
            "subject_id": subject_id,
        }


class ResourceSerializer(serializers.Serializer):
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
