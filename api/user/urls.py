from django.urls import re_path

from api.user.views import (
    UserView,
    ChangePasswordView,
    ForgotPasswordView
)

app_name = "api.user"

urlpatterns = [
    # re_path(r"^token-auth/$", ObtainJSONWebToken.as_view(), name="token_auth"),
    # re_path(r"^token-refresh/$", RefreshJSONWebToken.as_view(), name="token_refresh"),
    # re_path(r"^token-verify/$", VerifyJSONWebToken.as_view(), name="token_verify"),
    re_path(
        r"^forgot-password$",
        ForgotPasswordView.as_view(),
        name="send_reset_password_email",
    ),
    # re_path(r"^reset-password/$", ResetPasswordView.as_view(), name="reset_password"),
    re_path(
        r"^change-password/$", ChangePasswordView.as_view(), name="change_password"
    ),
    re_path(r"^$", UserView.as_view(), name="index"),
]
