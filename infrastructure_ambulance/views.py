from django.shortcuts import render

from rest_framework import generics
from .models import InfrastructureProject
from .Serializers import InfrastructureProjectSerializer
from .forms import InfrastructureProjectForm


class InfrastructureProjectList(generics.ListCreateAPIView):
    queryset = InfrastructureProject.objects.all()
    serializer_class = InfrastructureProjectSerializer


class InfrastructureProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InfrastructureProject.objects.all()
    serializer_class = InfrastructureProjectSerializer


def project_list(request):
    projects = InfrastructureProject.objects.all()
    return render(request, "project_list.html", {"projects": projects})


def project_submission(request):
    if request.method == "POST":
        form = InfrastructureProjectForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InfrastructureProjectForm()

    return render(request, "project_submission.html", {"form": form})
