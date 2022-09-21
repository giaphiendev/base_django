from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import UserType
from custom_service.models.ModelTechwiz import Student


class GetListStudentByClassView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        class_id = request.GET.get('class_id')
        if class_id is None:
            return Response({'payload': []}, status=200)
        list_student = Student.objects.filter(my_class_id=class_id).values_list(
            'id',
            'user__first_name',
            'user__last_name'
        )
        list_student_res = []
        for student in list_student:
            list_student_res.append({
                'id': student[0],
                'name': student[1] + " " + student[2]
            })
        data = {
            'list_user': list_student_res
        }
        return Response({'payload': data}, status=200)


class GetStudentIdFromParentView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        role = request.user.role
        if role is None or role != UserType.PARENT:
            return Response({"payload": []}, status=200)
        list_student = Student.objects.filter(parent_id=request.user.id).select_related('my_class').select_related(
            'user').values('id', 'my_class__name', 'user__last_name', 'user__first_name', 'user__date_of_birth')
        res = []
        for item in list_student:
            res.append({
                "id": item['id'],
                "class_name": item['my_class__name'],
                "full_name": item['user__first_name'] + " " + item['user__last_name'],
                "date_of_birth": item['user__date_of_birth'],
            })
        return Response({'payload': res}, status=200)
