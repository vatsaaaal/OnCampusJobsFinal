from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Jobs, name="jobs_list"),
    path('search', views.search, name="search"),
    path('<int:i_id>', views.detail, name='detail'),
    path('apply/<int:job_id>', views.apply, name='apply'),
    path('applications', views.applications, name='applications'),
    path('applications/<int:application_id>', views.application_detail, name='application_detail'),
    path('byyou/', views.allJobs, name='allJobs'),
    path('byyou/<int:job_id>', views.applicantList, name='applicantList'),
    path('byyou/applications/<int:application_id>', views.applicationDetailEmployer, name='applicationDetailEmployer'),
    path('<int:application_id>/accepted', views.decisionAccept, name='decisionAccept'),
    path('<int:application_id>/rejected', views.decisionDecline, name='decisionDecline'),
    path('createJob/', views.addJob, name='createJob'),
    path('editJob/<int:job_id>', views.editJob, name='editJob'),
    path('removeJob/<int:job_id>', views.removeJob, name='removeJob')
    ]