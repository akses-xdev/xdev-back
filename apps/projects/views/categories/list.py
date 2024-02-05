from rest_framework import permissions, generics

from apps.projects.models import Category
from apps.projects.serializers import CategorySerializer


class ListCategoryAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer