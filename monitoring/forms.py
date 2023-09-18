from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ProblemReport


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # Add any additional fields you want for registration
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name")


class ProblemReportForm(forms.ModelForm):
    class Meta:
        model = ProblemReport
        fields = ["type", "description", "location"]
