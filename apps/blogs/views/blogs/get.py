from rest_framework import generics, permissions

from apps.blogs.models import Blog
from apps.blogs.serializers import BlogSerializer


class GetBlogAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"