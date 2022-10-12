from django.urls import re_path

from api.revisionClass.views import (
    GetRevision,
    UpdateTimeTableView,
    GetListRevisonView,
    DetailView
)

app_name = "api.revision"

urlpatterns = [
    re_path(r"^$", GetRevision.as_view(), name="index"),
    re_path(r"^time-table/(?P<time_table_id>[0-9]+)$", UpdateTimeTableView.as_view(), name="update_revision"),
    re_path(r"^admin/$", GetListRevisonView.as_view(), name="index"),
    re_path(r"^admin/(?P<revision_id>[0-9]+)$", DetailView.as_view(), name="detail"),
]
