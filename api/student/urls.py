from django.urls import re_path

from api.student.views import (
    GetListStudetnByClassView
)

app_name = "api.student"

urlpatterns = [
    re_path(r"^$", GetListStudetnByClassView.as_view(), name="index")
]
