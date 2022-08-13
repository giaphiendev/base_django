from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import FeedBackSerializer
from core.decorators import validate_body
from core.models import UserType
from custom_service.handlers.grade import GradeHandle
from custom_service.models.ModelTechwiz import Student
from custom_service.task import send_feedback_by_email, send_report_mark, send_info_revision_class


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
            }
            send_report_mark.delay(data)

        elif role == UserType.PARENT:
            student_id = request.GET.get('student_id')
            data = {
                "email": email,
                "term1": GradeHandle().get_grade_family(student_id, 1),
                "term2": GradeHandle().get_grade_family(student_id, 2),
            }
            send_report_mark.delay(data)
        return Response({"payload": None}, status=200)


class SendInfoRevisionClassView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        email = request.user.email
        data = {
            "email": email
        }
        send_info_revision_class.delay(data)
        return Response({"payload": None}, status=200)
