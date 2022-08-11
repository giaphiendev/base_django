from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import User
from .crud import RevisionHandler
from custom_service.models.ModelTechwiz import Student


class GetRevision(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        student_id = 1
        stu = Student.objects.get(pk=student_id)
        # validate here
        # grade_report = ReportHandle().get_report_grade(stu)
        revision_class = RevisionHandler.get_revision(stu)
        data = {
            'revision_class': revision_class
        }
        return Response(data, status=200)
