from rest_framework import serializers
from .models import ProblemReport


class ProblemReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemReport
        fields = "__all__"
