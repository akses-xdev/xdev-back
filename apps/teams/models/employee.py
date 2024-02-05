from django.db import models
from apps.teams.models import Role, Technology


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatars/')
    telegram = models.CharField(max_length=100, blank=True, null=True)
    dev_level = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    tech_stack = models.ManyToManyField(Technology)

    def __str__(self):
        return self.email