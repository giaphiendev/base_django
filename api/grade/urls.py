from django.urls import re_path

from api.grade.views import (
    CreateGradeView,
    GetClassSubjectView,
    GetInputGradeView,
    GetSubjectView,
)

app_name = "api.grade"

urlpatterns = [
    re_path(r"^$", CreateGradeView.as_view(), name="create_grade"),
    re_path(r"^get-class-subject$", GetClassSubjectView.as_view(), name="get_class_subject"),
    re_path(r"^get-input-grade$", GetInputGradeView.as_view(), name="get_input_grade"),
    re_path(r"^get-subject$", GetSubjectView.as_view(), name="get_subject"),
]
