from django.contrib import admin
from .models import InfrastructureProject


@admin.register(InfrastructureProject)
class InfrastructureProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "progress", "cost", "development_period", "completion_time")
    search_fields = ("name",)  # Add any fields you want to search by
    list_filter = ("progress",)  # Add any fields you want to filter by
