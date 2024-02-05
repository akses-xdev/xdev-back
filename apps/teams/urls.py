from django.urls import path

from apps.teams import views

urlpatterns = [
    path('employees/create/', views.CreateEmployeeView.as_view(), name='create_employee'),
    path('employees/delete/<int:id>/', views.DeleteEmployeeAPIView.as_view(), name='delete_employee'),
    path("roles/list/", views.ListRolesAPIView.as_view(), name='list_roles'),
    path("technology/list/", views.TechnologyListAPIView.as_view(), name='list_technology'),
]