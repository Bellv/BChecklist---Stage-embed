import datetime

from django.db import models
from django.utils import timezone

class ProjectData(models.Model):
	project_name = models.CharField(max_length=30)
	project_date = models.DateTimeField('date published')
	project_status = models.BooleanField(default=False)
	def __str__(self):
		return self.project_name
	def was_published_recently(self):
		return self.project_date >= timezone.now() - datetime.timedelta(days=1)

class StageData(models.Model):
	project_data = models.ForeignKey(ProjectData, on_delete=models.CASCADE)
	stage_name = models.CharField(max_length=30)
	Stage_data = models.CharField(max_length=5)
	def __str__(self):
		return self.stage_name

class ChecklistData(models.Model):
	stage_data = models.ForeignKey(StageData, on_delete=models.CASCADE)
	detail = models.CharField(max_length=30)
	checklist_status = models.BooleanField(default=False)
	def __str__(self):
		return self.detail