from django.contrib import admin

from workers.models import Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "team_id", "salary", "specialization")
    list_filter = ("team_id", "specialization")
    ordering = ("full_name",)
