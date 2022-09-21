from rest_framework import serializers

from custom_service.models.ModelTechwiz import MyClass


class MyClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyClass
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
        }


class PutMyClassSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
