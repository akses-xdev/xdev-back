from rest_framework import serializers

from apps.teams.models import Employee
from .technology_serializer import TechnologySerializer
from .role_serializer import RoleSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ListEmployeeSerializer(EmployeeSerializer):
    role = RoleSerializer()
    tech_stack = TechnologySerializer(many=True)
