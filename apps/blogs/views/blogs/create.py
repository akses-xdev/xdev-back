from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from apps.blogs.models import Blog
from apps.blogs.serializers import BlogSerializer


class CreateBlogView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)