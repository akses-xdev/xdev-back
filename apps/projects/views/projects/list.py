from rest_framework import permissions, generics

from apps.projects.models import Project
from apps.projects.serializers import ListProjectsSerializer


class ListProjectAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Project.objects.all()
    serializer_class = ListProjectsSerializer