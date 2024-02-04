from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User


class LoginSerializer(serializers.Serializer): # noqa
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = None
        if '@' in data['email']:
            user = User.objects.filter(email=data['email']).first()

        if user and user.check_password(data['password']):
            refresh = RefreshToken.for_user(user)
            return {
                'id': user.id,
                'email': user.email,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        raise serializers.ValidationError('Incorrect email or password')