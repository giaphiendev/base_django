from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import User
from .crud import RevisionHandler
from custom_service.models.ModelTechwiz import Student


class GetRevision(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        student_id = request.GET.get('student_id', None)
        if student_id is None:
            return Response({'payload': []}, status=200)
        # validate here
        revision_class = RevisionHandler().get_revision_optimize(student_id)
        data = {
            'revision_class': revision_class
        }
        return Response(data, status=200)
