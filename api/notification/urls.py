from django.urls import re_path

from api.notification.views import (
    AddNewDeviceTokenView,
    PushNotificationView,
)

app_name = "api.notification"

urlpatterns = [
    re_path(r"^$", AddNewDeviceTokenView.as_view(), name="index"),
    re_path(r"^push-message$", PushNotificationView.as_view(), name="push_notification"),
]
