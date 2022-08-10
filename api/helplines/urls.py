from django.urls import re_path

from api.helplines.views import (
    GetListHelpLinesView
)

app_name = "api.helplines"

urlpatterns = [
    re_path(r"^$", GetListHelpLinesView.as_view(), name="index")
]
