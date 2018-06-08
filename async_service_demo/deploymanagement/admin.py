# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from djcelery.models import TaskMeta, TaskState


# Register your models here.
class TaskMetaAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'status', 'date_done', 'result', 'meta', 'traceback')
    search_fields = ('task_id', 'status',)
    readonly_fields = ('result',)
    list_filter = ('status',)


class TaskMetaAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'status', 'date_done', 'result', 'meta', 'traceback')
    search_fields = ('task_id', 'status',)
    readonly_fields = ('result',)
    list_filter = ('status',)


admin.site.register(TaskMeta, TaskMetaAdmin)
