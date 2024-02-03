from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.users.managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
