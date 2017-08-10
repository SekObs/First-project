from django.contrib import admin

from ticket.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'schedule_date', 'colored_due_date', 'remaining_days')

admin.site.register(Task, TaskAdmin)
