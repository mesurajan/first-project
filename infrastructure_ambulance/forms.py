from django import forms
from .models import InfrastructureProject


class InfrastructureProjectForm(forms.ModelForm):
    class Meta:
        model = InfrastructureProject
        fields = ["project_name", "description", "location"]
