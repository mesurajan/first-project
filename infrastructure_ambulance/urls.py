from django.urls import path
from .views import (
    InfrastructureProjectList,
    InfrastructureProjectDetail,
    project_list,
    project_submission,
)

urlpatterns = [
    path("projects/", InfrastructureProjectList.as_view(), name="project-list"),
    path(
        "projects/<int:pk>/",
        InfrastructureProjectDetail.as_view(),
        name="project-detail",
    ),
    path("submit/", project_submission, name="project_submission"),
    path("list/", project_list, name="project_list"),
]
