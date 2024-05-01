from django.db import models


class Application(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    description = models.TextField()
    telegram = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.username}"
