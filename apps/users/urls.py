from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
]