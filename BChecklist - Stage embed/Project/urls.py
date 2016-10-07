from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_id>[0-9]+)/$', views.projectdetail, name='projectdetail'),
    url(r'^(?P<project_id>[0-9]+)/project/$', views.checklistdetail, name='checklistdetail'),
]