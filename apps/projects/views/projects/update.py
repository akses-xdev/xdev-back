from rest_framework import permissions, generics

from apps.projects.models import Project
from apps.projects.serializers import ProjectSerializer


class UpdateProjectAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "id"