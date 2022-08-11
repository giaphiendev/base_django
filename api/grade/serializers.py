from rest_framework import serializers


class PostGradeSerializer(serializers.Serializer):
    mark = serializers.FloatField()
    description = serializers.CharField(required=False)
    exam = serializers.IntegerField()
    student = serializers.IntegerField()


class PutPostSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=False)
