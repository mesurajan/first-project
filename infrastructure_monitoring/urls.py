"""
URL configuration for infrastructure_monitoring project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("servers/", views.server_list, name="server_list"),
    path("", views.index, name="index"),
    path("servers/<int:server_id>/", views.server_detail, name="server_detail"),
    path("devices/", views.network_device_list, name="device_list"),
    path("devices/<int:device_id>/", views.network_device_detail, name="device_detail"),
    path("monitoring/", include("monitoring.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("home/", include("home.urls")),
    path("api/", include("infrastructure_ambulance.urls")),
]
