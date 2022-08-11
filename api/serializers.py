from rest_framework import serializers


class FeedBackSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
