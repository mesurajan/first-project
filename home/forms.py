
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ProblemReport


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # Add any additional fields you want for registration
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )


class LoginForm(AuthenticationForm):
    pass


class ProblemReportForm(forms.ModelForm):
    class Meta:
        model = ProblemReport
        fields = ["report_type", "description", "location"]
