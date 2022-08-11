import datetime

from rest_framework import serializers

from core.models import UserType
from custom_service.models.ModelTechwiz import NameExam, TermStatus, Grade, ClassTeacherSubject


class GetGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"


class GetClassSubjectSerializer(serializers.Serializer):
    class Meta:
        model = ClassTeacherSubject
        fields = '__all__'

    def to_representation(self, instance):
        if UserType.STUDENT == self.context:
            return {
                'subject': {
                    'id': instance.subject.id,
                    'name': instance.subject.name,
                },
            }
        return {
            'class': {
                'id': instance.my_class.id,
                'name': instance.my_class.name,
            },
            'subject': {
                'id': instance.subject.id,
                'name': instance.subject.name,
            },
        }


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
