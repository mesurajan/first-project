from django.urls import path
from .views import ProblemReportList
from . import views

urlpatterns = [
    path("servers/", views.server_list, name="server_list"),
    path("servers/<int:server_id>/", views.server_detail, name="server_detail"),
    path("devices/", views.network_device_list, name="network_device_list"),
    path(
        "devices/<int:device_id>/",
        views.network_device_detail,
        name="network_device_detail",
    ),
    path("", views.index, name="index"),
    path(
        "api/problem_reports/",
        views.ProblemReportList.as_view(),
        name="problem_report_list_api",
    ),
    path("login/", views.CustomLoginView, name="login"),
    path("logout/", views.CustomLogoutView, name="logout"),
    path("signup/", views.register, name="register"),
]
