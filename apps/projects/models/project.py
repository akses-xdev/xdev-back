from django.db import models

from apps.projects.models import Category


class Project(models.Model):
    title = models.CharField(max_length=255)
    preview = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='projects_poster/', blank=True, null=True)

    def __str__(self):
        return self.title
