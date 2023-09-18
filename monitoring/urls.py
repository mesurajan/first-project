from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import SignupView
from . import views
from .views import ProblemReportAPI

urlpatterns = [
    path("items/", views.monitor_item_list, name="monitor_item_list"),
    # User authentication URLs
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("report_problem/", views.report_problem, name="report_problem"),
    path("report_success/", views.report_success, name="report_success"),
    path("api/problem_reports/", ProblemReportAPI.as_view(), name="problem_report_api"),
    path(
        "project_info_submission/",
        views.project_info_submission,
        name="project_info_submission",
    ),
]
