from django.urls import re_path

from api.grade.views import (
    CreateGradeView
)

app_name = "api.grade"

urlpatterns = [
    re_path(r"^$", CreateGradeView.as_view(), name="create_grade"),
]
