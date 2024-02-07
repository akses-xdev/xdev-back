from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from x_dev.yasg import urlpatterns as doc_url

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/users/", include("apps.users.urls")),
    path("api/", include("apps.teams.urls")),
    path("api/", include("apps.projects.urls")),
    path("api/", include("apps.applications.urls")),
]

urlpatterns += i18n_patterns(
    path("api/", include("apps.blogs.urls")),
)

urlpatterns += doc_url

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)