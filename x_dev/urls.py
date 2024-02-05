from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/users/", include("apps.users.urls")),
    path("api/", include("apps.teams.urls")),

    path("i18n/", include("django.conf.urls.i18n")),
]