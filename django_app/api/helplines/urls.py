from django.urls import re_path

from api.helplines.views import (
    GetListHelpLinesView,
    # CreateView,
    DetailView,
)

app_name = "api.helplines"

urlpatterns = [
    re_path(r"^$", GetListHelpLinesView.as_view(), name="index"),
    re_path(r"^(?P<helplines_id>[0-9]+)$", DetailView.as_view(), name="detail"),
]
