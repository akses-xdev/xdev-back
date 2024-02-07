from rest_framework import generics, permissions

from apps.projects.models import Project
from apps.projects.serializers import ListProjectsSerializer


class GetProjectAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Project.objects.all()
    serializer_class = ListProjectsSerializer
    lookup_field = "id"