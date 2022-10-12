from rest_framework import serializers

from custom_service.models.ModelTechwiz import TimeTable


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
        }


class PutSerializer(serializers.Serializer):
    day_of_week = serializers.IntegerField()
    end_time = serializers.TimeField()
    start_time = serializers.TimeField()
