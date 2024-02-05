from rest_framework import permissions, generics

from apps.blogs.models import Blog
from apps.blogs.serializers import BlogSerializer


class UpdateBlogAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"