from django.urls import path

from api.v1.workers.views import WorkerDetailAPIView, WorkerInTeamListAPIView
from workers.apps import WorkersConfig

app_name = WorkersConfig.name

urlpatterns = [
    path(
        "team/<int:team_id>/WorkerList/",
        WorkerInTeamListAPIView.as_view(),
        name="worker-list",
    ),
    path("worker/<int:pk>/", WorkerDetailAPIView.as_view(), name="worker-detail"),
]
