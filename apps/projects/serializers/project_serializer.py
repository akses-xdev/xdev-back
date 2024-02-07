from rest_framework import serializers

from apps.projects.models import Project
from .categories_serializer import CategorySerializer


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"


class ListProjectsSerializer(ProjectSerializer):
    category = CategorySerializer

