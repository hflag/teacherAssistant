from django.contrib import admin
from .models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['teacher_name', 'course_name', 'class_name', 'room_name', 'week', 'order']


admin.site.register(Schedule, ScheduleAdmin)