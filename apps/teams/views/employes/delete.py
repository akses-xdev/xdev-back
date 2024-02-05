from rest_framework import generics, permissions

from apps.teams.models import Employee


class DeleteEmployeeAPIView(generics.DestroyAPIView):
    permissions = [permissions.IsAdminUser]
    queryset = Employee.objects.all()
    lookup_field = "id"