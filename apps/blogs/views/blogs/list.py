from rest_framework import permissions, generics

from apps.blogs.models import Blog
from apps.blogs.serializers import BlogSerializer


class ListBlogAPIView(generics.ListAPIView):
    permissions = [permissions.AllowAny]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer