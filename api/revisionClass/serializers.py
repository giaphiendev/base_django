from rest_framework import serializers

from custom_service.models.ModelTechwiz import RevisionClass


class RevisionClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevisionClass
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
        }


class PutRevisionClassSerializer(serializers.Serializer):
    time_start = serializers.DateTimeField()
    time_end = serializers.DateTimeField()
    status = serializers.BooleanField(default=1)
    subject = serializers.IntegerField()
    teacher = serializers.IntegerField()


class PutTimeTableSerializer(serializers.Serializer):
    time_table_id = serializers.IntegerField()
    day_of_week = serializers.IntegerField()
    end_time = serializers.TimeField()
    start_time = serializers.TimeField()
