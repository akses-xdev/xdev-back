from rest_framework import generics, permissions

from apps.teams.models import Employee
from apps.teams.serializers import ListEmployeeSerializer


class GetEmployeeAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Employee.objects.all()
    serializer_class = ListEmployeeSerializer
    lookup_field = "id"