from rest_framework import permissions, generics

from apps.teams.models import Employee
from apps.teams.serializers import ListEmployeeSerializer


class ListEmployeeAPIView(generics.ListAPIView):
    permissions = [permissions.AllowAny]
    serializer_class = ListEmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        role = self.request.query_params.get('role')
        if role:
            queryset = queryset.filter(role__id=role)
        return queryset