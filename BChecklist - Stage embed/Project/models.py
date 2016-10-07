import datetime

from django.db import models
from django.utils import timezone

class ProjectData(models.Model):
	project_name = models.CharField(max_length=30)
	project_date = models.DateTimeField('date published')
	project_stage_max = models.IntegerField(default=0)
	project_status = models.BooleanField(default=False)
	def __str__(self):
		return self.project_name
	def was_published_recently(self):
		return self.project_date >= timezone.now() - datetime.timedelta(days=1)

class ChecklistData(models.Model):
	projectdata = models.ForeignKey(ProjectData, on_delete=models.CASCADE)
	detail = models.CharField(max_length=30)
	current_stage = models.IntegerField(default=0)
	checklist_status = models.BooleanField(default=False)
	def __str__(self):
		return self.detail

	