from django.urls import path

from apps.projects import views

urlpatterns = [
    path('projects/categories/list/', views.ListCategoryAPIView.as_view(), name='category_list')
    # path('blogs/create/', views.CreateBlogView.as_view(), name='create_blogs'),
    # path('blogs/list/', views.ListBlogAPIView.as_view(), name='list_blog'),
    # path('blogs/delete/<int:id>/', views.DeleteBlogAPIView.as_view(), name='delete_blog'),
    # path('blogs/update/<int:id>/', views.UpdateBlogAPIView.as_view(), name='update_blog'),
    # path('blogs/detail/<int:id>/', views.GetBlogAPIView.as_view(), name='detail_blog'),
]