from django.urls import path
from .views import ProblemReportList
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("server_list/", views.server_list, name="server_list"),
    path("server_detail/<int:server_id>/", views.server_detail, name="server_detail"),
    path("device_list/", views.network_device_list, name="device_list"),
    path(
        "device_detail/<int:device_id>/",
        views.network_device_detail,
        name="device_detail",
    ),
    path("report_problem/", views.ProblemReportList.as_view(), name="report_problem"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("signup/", views.register, name="register"),
]
