from rest_framework import permissions, generics

from apps.projects.models import Project
from apps.projects.serializers import ListProjectsSerializer


class ListProjectAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ListProjectsSerializer

    def get_queryset(self):
        categories_query = self.request.query_params.getlist('category', '')

        if categories_query:
            queryset = Project.objects.filter(category__name__in=categories_query)
        else:
            queryset = Project.objects.all()

        return queryset