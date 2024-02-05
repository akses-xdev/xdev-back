from rest_framework import serializers

from apps.teams.models import Technology


class TechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = Technology
        fields = "__all__"

