from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.decorators import validate_body
from core.models import User, UserType
from .crud import RevisionHandler
from custom_service.models.ModelTechwiz import Student
from .serializers import PutTimeTableSerializer


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


class UpdateTimeTableView(APIView):
    permission_classes = (IsAuthenticated,)

    @validate_body(PutTimeTableSerializer)
    def put(self, request, revision_id, data):
        role = request.user.role
        if role is None or role != UserType.TEACHER:
            return Response({'error': {"message": "You have no permission to go"}}, status=200)
        # validate here
        RevisionHandler().update_revision(revision_id, data)

        return Response({'payload': None}, status=200)
