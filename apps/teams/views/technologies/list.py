from rest_framework import permissions, generics

from apps.teams.models import Technology
from apps.teams.serializers import TechnologySerializer


class TechnologyListAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
