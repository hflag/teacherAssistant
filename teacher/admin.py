from django.contrib import admin
from .models import Schedule, Banji, Act, Student, Course


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'course', 'banji', 'room_name', 'week', 'order']


admin.site.register(Schedule, ScheduleAdmin)


class BanjiAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']

admin.site.register(Banji, BanjiAdmin)


class ActAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']

admin.site.register(Act, ActAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['No', 'name', 'sex']

admin.site.register(Student, StudentAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Course, CourseAdmin)