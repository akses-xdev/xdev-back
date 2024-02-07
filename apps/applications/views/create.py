from rest_framework import permissions, generics

from apps.applications.models import Application
from apps.applications.serializers import ApplicationSerializer


class CreateApplicationAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer