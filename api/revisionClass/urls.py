from django.urls import re_path

from api.revisionClass.views import (
    GetRevision,
    UpdateTimeTableView
)

app_name = "api.revision"

urlpatterns = [
    re_path(r"^$", GetRevision.as_view(), name="index"),
    re_path(r"^time-table/(?P<revision_id>[0-9]+)$", UpdateTimeTableView.as_view(), name="update_revision"),
]
