from rest_framework import serializers

from custom_service.models.ModelTechwiz import HelpLine


class HelpLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpLine
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
        }


class PutHelpLineSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=15)
    type = serializers.CharField(max_length=50)