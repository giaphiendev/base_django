from django.urls import re_path

from api.subject.views import (
    GetListSubjectView,
    DetailSubjectView,
)

app_name = "api.subject"

urlpatterns = [
    re_path(r"^$", GetListSubjectView.as_view(), name="index"),
    re_path(r"^(?P<subject_id>[0-9]+)$", DetailSubjectView.as_view(), name="detail"),
]
