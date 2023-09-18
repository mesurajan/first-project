from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm
from collections import UserDict, UserList
from monitoring.models import MonitorItem  # Correct import
from django.views.generic.edit import FormView

from django.shortcuts import render, get_object_or_404
from home.models import Server

from .models import Server  # Remove redundant import

from . import views
from .models import Server, NetworkDevice
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from home.models import NetworkDevice, ProblemReport  # Correct import
from home.Serializers.Serializers import ProblemReportSerializer  # Correct import
from django.http import HttpResponse
from .forms import UserCreationForm, LoginForm


def index(request):
    return render(request, "home/index.html")


def server_list(request):
    servers = Server.objects.all()
    return render(request, "home/server_list.html", {"servers": servers})


def server_detail(request, server_id):
    server = get_object_or_404(Server, id=server_id)
    return render(request, "home/server_detail.html", {"server": server})


class ProblemReportList(APIView):
    def get(self, request):
        reports = ProblemReport.objects.all()
        serializer = ProblemReportSerializer(reports, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProblemReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login view using the built-in LoginView
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = "home/login.html"


# Logout view using the built-in LogoutView
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")


# Example of a view that requires authentication
@login_required
def profile(request):
    # Your profile view logic here
    return render(request, "home/profile.html")


def network_device_list(request):
    devices = NetworkDevice.objects.all()
    return render(request, "home/device_list.html", {"devices": devices})


def network_device_detail(request, device_id):
    device = get_object_or_404(NetworkDevice, id=device_id)
    return render(request, "home/device_detail.html", {"device": device})


# Registration view
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # You can customize the success redirect URL as per your project's needs
            return redirect(
                "login"
            )  # Redirect to the login page after successful registration
    else:
        form = CustomUserCreationForm()

    return render(request, "home/signup.html", {"form": form})
