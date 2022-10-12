from django.urls import re_path

from .views import (
    GetListView,
    DetailView,
)

app_name = "api.class_teacher_subject"

urlpatterns = [
    re_path(r"^revision/(?P<revision_id>[0-9]+)$", GetListView.as_view(), name="index"),
    re_path(r"^(?P<id>[0-9]+)$", DetailView.as_view(), name="detail"),
]
