from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import User
from custom_service.handlers.report import ReportHandle
from custom_service.models.ModelTechwiz import Student


class GetReportMark(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        student_id = 1
        # stu = Student.objects.get(pk=student_id)
        # validate here
        # grade_report = ReportHandle().get_report_grade(stu)
        data = {
            'student_id': student_id
        }
        return Response(data, status=200)
