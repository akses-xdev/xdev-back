from django.db.models import Q
from rest_framework import permissions, generics
from django.utils.translation import get_language

from apps.blogs.models import Blog
from apps.blogs.serializers import BlogSerializer


class ListBlogAPIView(generics.ListAPIView):
    permissions = [permissions.AllowAny]
    serializer_class = BlogSerializer

    def get_queryset(self):
        language = get_language()
        search_query = self.request.query_params.get('search', '')

        if search_query:
            queryset = Blog.objects.filter(
                Q(**{f'title_{language}__icontains': search_query}) |
                Q(**{f'description_{language}__icontains': search_query}) |
                Q(**{f'content_{language}__icontains': search_query})
            )
        else:
            queryset = Blog.objects.all()

        return queryset