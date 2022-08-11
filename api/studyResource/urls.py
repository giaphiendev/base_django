from django.urls import re_path

from api.studyResource.views import (
    GetResource,
    DetailResourceView
)

app_name = "api.studyResource"

urlpatterns = [
    re_path(r"^$", GetResource.as_view(), name="index"),
    re_path(r"^(?P<resource_id>[0-9]+)$", DetailResourceView.as_view(), name="detail"),
]
