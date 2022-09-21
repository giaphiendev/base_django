from django.urls import re_path

from api.student.views import (
    GetListStudentByClassView, GetStudentIdFromParentView
)

app_name = "api.student"

urlpatterns = [
    re_path(r"^list$", GetListStudentByClassView.as_view(), name="index"),
    re_path(r"^get-student-id$", GetStudentIdFromParentView.as_view(), name="get_student_from_parent")
]
