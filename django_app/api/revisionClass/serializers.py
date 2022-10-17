from rest_framework import serializers

from custom_service.models.ModelTechwiz import RevisionClass


class RevisionClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevisionClass
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
        }


class GetRevisionClassSerializer(serializers.Serializer):
    info = serializers.SerializerMethodField()

    def get_info(self, instance):
        time_start = instance.time_start
        time_end = instance.time_end
        status = instance.status

        subject_name = instance.subject.name
        subject_id = instance.subject.id
        teacher_id = instance.teacher.id
        teacher_first_name = instance.teacher.first_name
        teacher_last_name = instance.teacher.last_name
        return {
            "time_start": time_start,
            "time_end": time_end,
            "status": status,
            "subject_name": subject_name,
            "subject_id": subject_id,
            "teacher_id": teacher_id,
            "teacher_first_name": teacher_first_name,
            "teacher_last_name": teacher_last_name,
        }


class PutRevisionClassSerializer(serializers.Serializer):
    time_start = serializers.DateTimeField()
    time_end = serializers.DateTimeField()
    status = serializers.BooleanField(default=1)
    subject = serializers.IntegerField()
    teacher = serializers.IntegerField()


class PutTimeTableSerializer(serializers.Serializer):
    # time_table_id = serializers.IntegerField()
    day_of_week = serializers.IntegerField()
    end_time = serializers.TimeField()
    start_time = serializers.TimeField()
