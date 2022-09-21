from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.decorators import validate_body
from core.models import UserType
from custom_service.models.ModelTechwiz import Student, RevisionClass, ClassTeacherSubject, Subject
from .crud import RevisionHandler
from .serializers import PutTimeTableSerializer
from custom_service.task import send_notification_to_device_celery


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

    # @validate_body(PutTimeTableSerializer)
    def put(self, request, time_table_id):
        data = request.data
        role = request.user.role
        if role is None or role != UserType.TEACHER:
            return Response({'error': {"message": "You have no permission to go"}}, status=200)
        # validate here
        RevisionHandler().update_revision(time_table_id, data)

        # push_notification update revision class
        sub_id = RevisionClass.objects.filter(
            time_table_revision_class__id=time_table_id
        ).select_related('subject').values_list(
            'subject_id',
            flat=True
        )[:1]
        subject = Subject.objects.filter(id=sub_id[0]).first()

        class_teacher_subject = ClassTeacherSubject.objects.filter(
            subject_id=sub_id[0]
        ).values_list('my_class_id', flat=True)

        user_id = Student.objects.filter(
            my_class_id__in=class_teacher_subject
        ).select_related('user').values_list('user_id', flat=True)

        data_push_notification = {
            "title": f"Teacher {request.user.first_name} {request.user.last_name} \n Revision class schedule",
            "message": f"{subject.name}’s revision class schedule has been changed",
            "extra": {"created_at": datetime.now()},
            "user_id": list(set(user_id))
        }
        send_notification_to_device_celery.delay(data_push_notification)

        return Response({'payload': None}, status=200)