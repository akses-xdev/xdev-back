from django.urls import path

from apps.teams import views

urlpatterns = [
    path('employees/create/', views.CreateEmployeeView.as_view(), name='create_employee'),
    path("roles/list/", views.ListRolesAPIView.as_view(), name='list_roles'),
]