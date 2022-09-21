from django.urls import re_path

from api.report.views import (
    GetReportMark
)

app_name = "api.report"

urlpatterns = [
    re_path(r"^$", GetReportMark.as_view(), name="index"),
]
