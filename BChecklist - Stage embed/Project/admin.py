from django.contrib import admin

from .models import ProjectData, ChecklistData

admin.site.register(ProjectData)
admin.site.register(ChecklistData)