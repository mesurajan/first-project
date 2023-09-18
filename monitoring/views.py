from collections import UserDict, UserList
from django.shortcuts import render, redirect
from monitoring.models import MonitorItem

from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm
from .forms import ProblemReportForm
from .models import ProblemReport
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProblemReport
from .serializers import ProblemReportSerializer
from django.http import HttpResponse


def monitor_item_list(request):
    items = MonitorItem.objects.all()
    return render(request, "monitoring/monitor_item_list.html", {"items": items})


class SignupView(FormView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy(
        "login"
    )  # Redirect to login after successful registration


def form_valid(self, form):
    # Process the form data here (e.g., create a user)
    # You can access the form data via form.cleaned_data
    # After processing, you can log the user in if needed
    return FormView.form_valid(self, form)


def report_problem(request):
    if request.method == "POST":
        form = ProblemReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "report_success"
            )  # Redirect to a success page or relevant URL
    else:
        form = ProblemReportForm()
    return render(request, "monitoring/report_problem.html", {"form": form})


def infrastructure_ambulance(request):
    problems = ProblemReport.objects.all()  # Query reported problems
    return render(
        request, "monitoring/infrastructure_ambulance.html", {"problems": problems}
    )


class ProblemReportAPI(APIView):
    def get(self, request):
        reports = ProblemReport.objects.all()
        serializer = ProblemReportSerializer(reports, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProblemReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


def project_info_submission(request):
    if request.method == "POST":
        project_name = request.POST.get("projectName")
        description = request.POST.get("description")
        location = request.POST.get("location")

        # Process the form data (e.g., save it to a database)

        return render(
            request, "success.html"
        )  # Replace 'success.html' with the template you want to render after successful submission

    return render(
        request, "project_info_form.html"
    )  # Replace 'project_info_form.html' with the template containing your form


report_success = True


def report_problem(request):
    return render(
        request, "monitoring/report_problem.html", {"report_success": report_success}
    )


def report_success(request):
    return render(request, "monitoring/report_success.html")
