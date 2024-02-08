from rest_framework import permissions, generics

from apps.applications.models import Application
from apps.applications.serializers import ApplicationSerializer
from apps.shared.logic.email import send_email


class CreateApplicationAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        message = f'New application details:\n\nUsername: {instance.username}\nEmail: {instance.email}\nPhone number: {instance.phone_number}\nDescription: {instance.description}'
        try:
            send_email(message)
        except Exception:
            pass
        return instance