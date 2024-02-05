from rest_framework import generics, permissions

from apps.blogs.models import Blog


class DeleteBlogAPIView(generics.DestroyAPIView):
    permissions = [permissions.IsAdminUser]
    queryset = Blog.objects.all()
    lookup_field = "id"