from django.db import models

NULLABLE = {"blank": True, "null": True}


class Worker(models.Model):
    """
    Модель рабочего.
    """

    SPECIALIZATION_CHOICES = [
        ("1", "Черновая отделка"),
        ("2", "Чистовая отделка"),
        ("3", "Бригадир"),
        ("4", "Прораб")
    ]

    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    team_id = models.PositiveSmallIntegerField(**NULLABLE, verbose_name="Номер бригады")
    salary = models.PositiveIntegerField(verbose_name="Заработная плата")
    specialization = models.CharField(
        max_length=100, choices=SPECIALIZATION_CHOICES, default="3", verbose_name="Специализация"
    )

    class Meta:
        verbose_name = "Рабочий"
        verbose_name_plural = "Рабочие"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self.full_name=}, {self.team_id=}, {self.salary=}, {self.specialization=})")
