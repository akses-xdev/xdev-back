from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

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