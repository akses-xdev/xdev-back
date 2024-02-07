from django.urls import path

from apps.projects import views

urlpatterns = [
    path('projects/categories/list/', views.ListCategoryAPIView.as_view(), name='category_list'),
    path('projects/create/', views.CreateProjectView.as_view(), name='create_project'),
    path('projects/list/', views.ListProjectAPIView.as_view(), name='list_projects'),
    path('projects/delete/<int:id>/', views.DeleteProjectAPIView.as_view(), name='delete_project'),
    path('projects/update/<int:id>/', views.UpdateProjectAPIView.as_view(), name='update_project'),
    path('projects/detail/<int:id>/', views.GetProjectAPIView.as_view(), name='detail_project'),
]