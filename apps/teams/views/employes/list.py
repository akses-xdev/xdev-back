from rest_framework import permissions, generics

from apps.teams.models import Employee
from apps.teams.serializers import ListEmployeeSerializer


class ListEmployeeAPIView(generics.ListAPIView):
    permissions = [permissions.IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = ListEmployeeSerializer