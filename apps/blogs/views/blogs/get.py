from rest_framework import generics, permissions
from rest_framework.response import Response

from apps.blogs.models import Blog
from apps.blogs.serializers import BlogSerializer


class GetBlogAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"

    def increment_views(self, blog):
        blog.views += 1
        blog.save()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        self.increment_views(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class GetBlogByTitleAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "title"

    def increment_views(self, blog):
        blog.views += 1
        blog.save()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        self.increment_views(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)