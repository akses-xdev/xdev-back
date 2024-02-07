from rest_framework import generics, permissions

from apps.projects.models import Project


class DeleteProjectAPIView(generics.DestroyAPIView):
    permissions = [permissions.IsAdminUser]
    queryset = Project.objects.all()
    lookup_field = "id"