from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.revisionClass.crud import RevisionHandler
from api.serializers import FeedBackSerializer, ChatSerializer, NotificationChatSerializer
from core.decorators import validate_body
from core.models import UserType
from custom_service.handlers.grade import GradeHandle
from custom_service.models.ModelTechwiz import Student
from custom_service.redis_pub_sub import publish_data_on_redis
from custom_service.task import (
    send_feedback_by_email,
    send_report_mark,
    send_info_revision_class, notification_chat_celery,
)


class FeedBackView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FeedBackSerializer

    def get(self, request):
        email_dev = "hiencoday363@yopmail.com"
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            data['email'] = email_dev
            send_feedback_by_email.delay(data)
        return Response({"payload": None}, status=200)

    @validate_body(FeedBackSerializer)
    def post(self, request, data):
        email_dev = "hiencoday363@yopmail.com"
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            data['email'] = email_dev
            send_feedback_by_email.delay(data)
        return Response({"payload": None}, status=200)


class SendReportCardView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        email = request.user.email
        role = request.user.role
        if role is None:
            return Response({"payload": []}, status=200)
        elif role == UserType.STUDENT:
            student_id = Student.objects.filter(user_id=request.user.id).first().id
            data = {
                "email": email,
                "term1": GradeHandle().get_grade_family(student_id, 1),
                "term2": GradeHandle().get_grade_family(student_id, 2),
                "full_name": request.user.first_name + " " + request.user.last_name,
            }
            send_report_mark.delay(data)

        elif role == UserType.PARENT:
            student_id = int(request.data.get("student_id"))
            user = Student.objects.filter(
                id=student_id
            ).select_related('user').values('user__first_name', 'user__last_name')
            data = {
                "email": email,
                "term1": GradeHandle().get_grade_family(student_id, 1),
                "term2": GradeHandle().get_grade_family(student_id, 2),
                "full_name": user[0].get('user__first_name') + " " + user[0].get('user__last_name'),
            }
            send_report_mark.delay(data)
        return Response({"payload": None}, status=200)


class SendInfoRevisionClassView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        role = request.user.role
        if role != UserType.STUDENT:
            return Response({"error": 'You have no permission go forward!'}, status=400)
        student_id = Student.objects.filter(user_id=request.user.id).first().id
        list_time_table_res = RevisionHandler().get_revision_optimize(student_id)
        email = request.user.email
        data = {
            "email": email,
            'list_time_table_res': list_time_table_res
        }
        send_info_revision_class.delay(data)
        return Response({"payload": None}, status=200)


class SubmitChatView(APIView):
    permission_classes = (AllowAny,)

    @validate_body(ChatSerializer)
    def post(self, request, data):
        # type is function's name in chat_consumer
        context = {
            "message": data.get('message'),
            "receiver_id": data.get('receiver_id'),
        }
        publish_data_on_redis(context)

        return Response({"payload": None}, status=200)


class NotificationChatView(APIView):
    permission_classes = (AllowAny,)

    @validate_body(NotificationChatSerializer)
    def post(self, request, data):
        # type is function's name in chat_consumer
        notification_chat_celery.delay(data)

        return Response({"payload": None}, status=200)
