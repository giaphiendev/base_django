from django.urls import include, re_path, path
from django.http import HttpResponse
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static


def health(request):
    return HttpResponse("OK")


urlpatterns = (
        [
            re_path(r"^api/", include("api.urls", namespace="api")),
            re_path(r"^_health$", health, name="health_check"),
            path('admin/', admin.site.urls),
        ]
        + static(settings.MEDIA_URL_PATH, document_root=settings.MEDIA_ROOT)
)
