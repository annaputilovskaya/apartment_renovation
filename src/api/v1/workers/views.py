from rest_framework import generics

from workers.models import Worker
from workers.paginations import CustomPagination
from workers.serializers import WorkerSerializer


class WorkerInTeamListAPIView(generics.ListAPIView):
    """
    Контроллер списка рабочих бригады.
    """

    serializer_class = WorkerSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        team_id = self.kwargs[ "team_id"]
        return Worker.objects.filter(team_id=team_id)


class WorkerDetailAPIView(generics.RetrieveAPIView):
    """
    Контроллер детального представления рабочего.
    """

    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
