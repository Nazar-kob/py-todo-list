from django.contrib import admin

from task.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['content', 'datetime', 'deadline', 'is_done']
    filter_horizontal = ['tags']

