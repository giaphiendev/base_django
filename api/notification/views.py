from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from custom_service.handlers.push_notification import PushNotificationHandle
from custom_service.task import send_notification_to_device_celery


class AddNewDeviceTokenView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        if data.get('token'):
            device = PushNotificationHandle().add_push_notification_token(request.user, data)
            return Response({'payload': device.id}, status=200)
        return Response({"error": {"message": "missing data"}}, status=400)


class PushNotificationView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """
        args:
            data: {message: "message", extra: {}, user_id: 1}
        """
        data = request.data
        if data.get('user_id'):
            send_notification_to_device_celery.delay(data)
            return Response({'payload': None}, status=200)
        return Response({"error": {"message": "missing data"}}, status=400)
