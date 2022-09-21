from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.decorators import map_exceptions
from custom_service.errors import ERROR_STUDENT_NOT_FOUND
from custom_service.exceptions import StudentNotFound
from custom_service.handlers.report import ReportHandle


class GetReportMark(APIView):
    permission_classes = (IsAuthenticated,)

    @map_exceptions(
        {
            StudentNotFound: ERROR_STUDENT_NOT_FOUND,
        }
    )
    def get(self, request):
        student_id = 1
        grade_report = ReportHandle().get_report_grade(student_id)
        data = {
            'student_id': grade_report
        }
        return Response(data, status=200)
