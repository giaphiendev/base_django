import datetime

from rest_framework import serializers

from custom_service.models.ModelTechwiz import NameExam, TermStatus, Grade


class GetGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"


class PostGradeSerializer(serializers.Serializer):
    mark = serializers.FloatField()
    start_year = serializers.IntegerField(default=datetime.datetime.now().year)
    end_year = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)
    type_exam = serializers.ChoiceField(choices=NameExam.choices)
    term = serializers.ChoiceField(choices=TermStatus.choices)
    exam_date = serializers.DateField()

    teacher_id = serializers.IntegerField()
    subject_id = serializers.IntegerField()
    student_id = serializers.IntegerField()


class PutPostSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=False)
