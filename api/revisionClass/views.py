from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.decorators import validate_body
from core.models import UserType
from custom_service.models.ModelTechwiz import Student
from .crud import RevisionHandler
from .serializers import PutTimeTableSerializer


class GetRevision(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        role = request.user.role
        # validate here
        revision_class = []
        if role == UserType.TEACHER:
            # get revision by teacher
            revision_class = RevisionHandler().get_revision_by_teacher(request.user.id)
        elif role == UserType.STUDENT:
            student_id = Student.objects.filter(user_id=request.user.id).first().id
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
