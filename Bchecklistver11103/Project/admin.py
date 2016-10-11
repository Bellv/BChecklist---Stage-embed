from django.contrib import admin

from .models import ProjectData, ChecklistData, StageData

admin.site.register(ProjectData)
admin.site.register(ChecklistData)
admin.site.register(StageData)