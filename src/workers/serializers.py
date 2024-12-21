from rest_framework import serializers

from .models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    """
    Сериализатор работника.
    """

    class Meta:
        model = Worker
        fields = "__all__"
