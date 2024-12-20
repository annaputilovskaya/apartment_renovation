# Generated by Django 5.1.4 on 2024-12-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worker",
            name="specialization",
            field=models.CharField(
                choices=[
                    ("rough_finish", "Черновая отделка"),
                    ("fine_finish", "Чистовая отделка"),
                    ("brigadier", "Бригадир"),
                    ("forman", "Прораб"),
                ],
                default="brigadier",
                max_length=100,
                verbose_name="Специализация",
            ),
        ),
    ]