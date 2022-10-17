from rest_framework import serializers


class FeedBackSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()


class ChatSerializer(serializers.Serializer):
    message = serializers.CharField(required=True)
    receiver_id = serializers.IntegerField(required=True)


class NotificationChatSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    data = serializers.CharField()
    user_ids = serializers.ListSerializer(child=serializers.IntegerField(), required=True)
