from rest_framework import permissions, generics

from apps.teams.models import Role
from apps.teams.serializers import RoleSerializer


class ListRolesAPIView(generics.ListAPIView):
    queryset = Role.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RoleSerializer