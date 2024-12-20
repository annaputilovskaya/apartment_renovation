from django.urls import path

from api.v1.workers.views import WorkerInTeamList

urlpatterns = [
    path('team/<int:team_id>/WorkerList/', WorkerInTeamList.as_view(), name='worker-list'),
    ]
