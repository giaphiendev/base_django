import json
import redis

from django.conf import settings

redis_client = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    username=settings.REDIS_USERNAME,
    password=settings.REDIS_PASSWORD,
)


def publish_data_on_redis(json_data):
    redis_client.publish(settings.CHANNEL_CHAT_REDIS, json.dumps(json_data))
