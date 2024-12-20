from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from workers.models import Worker


class WorkerTestCase(APITestCase):
    def setUp(self):
        self.worker1 = Worker.objects.create(
            full_name="Тест 1",
            team_id=1,
            salary=10000,
            specialization="1"
        )
        self.worker2 = Worker.objects.create(
            full_name="Тест 2",
            team_id=2,
            salary=10000,
            specialization="2"
        )
        self.worker3 = Worker.objects.create(
            full_name="Тест 3",
            team_id=1,
            salary=12000
        )

    def test_worker_list(self):
        url = reverse("v1:worker-list", args=(self.worker1.team_id,))
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "full_name": "Тест 1",
                    "team_id": 1,
                    "salary": 10000,
                    "specialization": "1"
                },
                {
                    "id": 3,
                    "full_name": "Тест 3",
                    "team_id": 1,
                    "salary": 12000,
                    "specialization": "3"
                }
            ]
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_worker_retrieve(self):
        url = reverse("v1:worker-detail", args=(self.worker1.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("full_name"), self.worker1.full_name)