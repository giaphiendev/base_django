from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularJSONAPIView, SpectacularRedocView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .webhooks import urls as webhook_urls
from .auth import urls as auth_urls
from .user import urls as user_urls
from .report import urls as report_urls
from .grade import urls as post_urls
from .myClass import urls as myClass_urls
from .class_teacher_subject import urls as class_teacher_subject_urls
from .subject import urls as subject_urls
from .helplines import urls as helpline_urls
from .studyResource import urls as resource_urls
from .revisionClass import urls as revision_urls
from .student import urls as student_urls
from .time_table import urls as timetable_urls
from .notification import urls as notification_urls
from .views import (
    FeedBackView,
    SendReportCardView,
    SendInfoRevisionClassView,
    SubmitChatView,
    NotificationChatView,
)

app_name = "api"

schema_view = get_schema_view(
    openapi.Info(
        title="Jaseci API",
        default_version='v1',
        description="Welcome to the world of Jaseci",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="jason@jaseci.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = (
    [
        # swagger
        path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # <-- Here
        re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # <-- Here

        # drf_spectacular like swagger
        re_path(r"^schema.json$", SpectacularJSONAPIView.as_view(), name="json_schema"),
        re_path(
            r"^redoc$",
            SpectacularRedocView.as_view(url_name="api:json_schema"),
            name="redoc",
        ),
        # webhook
        path("webhooks/", include(webhook_urls, namespace="webhooks")),
        # my url
        path("auth/", include(auth_urls, namespace="auth")),
        path("user/", include(user_urls, namespace="user")),
        # demo api for post model
        path("grade/", include(post_urls, namespace="grade")),
        path("report/", include(report_urls, namespace="report")),
        path("myclass/", include(myClass_urls, namespace="myClass")),
        path("helplines/", include(helpline_urls, namespace="helplines")),
        path("class_teacher_subject/", include(class_teacher_subject_urls, namespace="class_teacher_subject")),
        path("studyresource/", include(resource_urls, namespace="resources")),
        path("revision/", include(revision_urls, namespace="revision")),
        path("student/", include(student_urls, namespace="student")),
        path("subject/", include(subject_urls, namespace="subject")),
        path("timetable/", include(timetable_urls, namespace="timetable")),
        # notification
        path("notification/", include(notification_urls, namespace="notification")),
        # send feedback
        re_path(r"^feedback$", FeedBackView.as_view(), name="feedback"),
        # send email report card
        re_path(r"^send-report-card$", SendReportCardView.as_view(), name="send_report_card"),
        re_path(r"^send-info-revision$", SendInfoRevisionClassView.as_view(), name="send_info_revision_class"),
        # api for submit chat
        re_path(r"^submit-chat$", SubmitChatView.as_view(), name="submit_chat"),
        re_path(r"^noti-chat$", NotificationChatView.as_view(), name="notification_chat"),
    ]
)
