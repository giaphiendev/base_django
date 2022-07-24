from django.urls import re_path

from api.post.views import (
    GetListPostView,
    DetailPostView
)

app_name = "api.post"

urlpatterns = [
    re_path(r"^$", GetListPostView.as_view(), name="index"),
    re_path(r"^(?P<post_id>[0-9]+)$", DetailPostView.as_view(), name="detail"),
]
