from django.urls import re_path

from api.myClass.views import (
    GetListMyClassView,
    DetailMyClassView,
)

app_name = "api.myClass"

urlpatterns = [
    re_path(r"^$", GetListMyClassView.as_view(), name="index"),
    re_path(r"^(?P<myClass_id>[0-9]+)$", DetailMyClassView.as_view(), name="detail"),
]
