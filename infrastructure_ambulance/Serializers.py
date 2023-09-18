from rest_framework import serializers
from .models import InfrastructureProject


class InfrastructureProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfrastructureProject
        fields = "__all__"
