from rest_framework import generics

from workers.models import Worker
from workers.serializers import WorkerSerializer


class WorkerInTeamList(generics.ListAPIView):
    """
    Контроллер списка сотрудников бригады.
    """

    serializer_class = WorkerSerializer

    def get_queryset(self):
        team_id = self.kwargs[ "team_id"]
        return Worker.objects.filter(team_id=team_id)
