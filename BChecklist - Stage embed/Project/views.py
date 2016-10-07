from django.shortcuts import render, Http404
from django.http import HttpResponse
from django.template import loader

from .models import ProjectData

def index(request):
	latest_project_list = ProjectData.objects.order_by('-project_date')
	template = loader.get_template('Project/index.html')
	context = {
		'latest_project_list': latest_project_list
	}
	return HttpResponse(template.render(context, request))

def projectdetail(request, project_id):
    try:
        project_Data_detail = ProjectData.objects.get(pk=project_id)
    except ProjectData.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'Project/projectdetail.html', {'project_data_detail': project_Data_detail})
    #return HttpResponse("Now On Project %s." % project_id)

def checklistdetail(request, project_id):
    response = "Now on checklist %s."
    return HttpResponse(response % project_id)