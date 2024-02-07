from django.urls import path

from apps.applications import views

urlpatterns = [
    path('applications/create/', views.CreateApplicationAPIView.as_view(), name='application_create'),
]