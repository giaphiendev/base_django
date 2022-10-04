from rest_framework import serializers


class FeedBackSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()


class ChatSerializer(serializers.Serializer):
    message = serializers.CharField(required=True)
    receiver_id = serializers.IntegerField(required=True)
