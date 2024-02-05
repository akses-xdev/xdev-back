from rest_framework import generics, permissions

from apps.teams.models import Employee


class DeleteEmployeeAPIView(generics.DestroyAPIView):
    permissions = [permissions.AllowAny]
    queryset = Employee.objects.all()
    lookup_field = "id"