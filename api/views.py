from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import FeedBackSerializer
from core.decorators import validate_body
from custom_service.task import send_feedback_by_email, send_report_mark


class FeedBackView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FeedBackSerializer

    @validate_body(FeedBackSerializer)
    def post(self, request, data):
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            data['email'] = "hiencoday363@yopmail.com"
            send_feedback_by_email.delay(data)
            # send_report_mark.delay(data)
        return Response({"payload": None}, status=200)


class SendReportCardView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = {
            "email": "hiencoday363@yopmail.com"
        }
        send_report_mark.delay(data)
        return Response({"payload": None}, status=200)
