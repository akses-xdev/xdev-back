from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from apps.teams.models import Employee
from apps.teams.serializers import EmployeeSerializer


class CreateEmployeeView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)