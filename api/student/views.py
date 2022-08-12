from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from custom_service.models.ModelTechwiz import Student


class GetListStudetnByClassView(APIView):
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
