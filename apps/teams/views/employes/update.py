from rest_framework import permissions, generics

from apps.teams.models import Employee
from apps.teams.serializers import EmployeeSerializer


class UpdateEmployeeAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "id"