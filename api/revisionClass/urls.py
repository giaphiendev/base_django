from django.urls import re_path

from api.revisionClass.views import (
    GetRevision
)

app_name = "api.revision"

urlpatterns = [
    re_path(r"^$", GetRevision.as_view(), name="index"),
]
