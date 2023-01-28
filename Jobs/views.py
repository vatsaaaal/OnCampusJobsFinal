from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Application
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
from django.contrib.auth.decorators import user_passes_test

def Jobs(request):
    job = Job.objects.all()
    new_dict ={}
    for item in job:
        new_dict[item] = item
    filter = JobFilter(request.GET, queryset = job)
    job = filter.qs
    return render(request, 'Jobs/jobs_list.html', {"jobs": job, "filter":filter})

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        if search:
            match = Job.objects.filter(Q(name__icontains=search) | Q(department__icontains=search))
            if match:
                return render(request, 'Jobs/search.html', {'match':match})
            else:
                return render(request, 'Jobs/search.html', {'error':'No Results Found'})
        else:
            return HttpResponseRedirect('Jobs/jobs_list.html')
    return render(request, 'Jobs/jobs_list.html')

def detail(request, i_id):
    job = get_object_or_404(Job, pk=i_id)
    return render(request, 'Jobs/job_detail.html', {'job':job})

@login_required
def apply(request, job_id):
    job_apply = get_object_or_404(Job, pk=job_id)
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    if request.method == 'POST':
        application = Application()
        application.job = job_apply
        application.user = user
        application.name = request.POST.get('name')
        application.email = user.email
        application.major = request.POST.get('major')
        application.year = request.POST.get('year')
        application.fit = request.POST.get('fit')
        application.resume = request.POST.get('resume')
        application.save()
        return redirect('jobs_list')
    return render(request, 'Jobs/apply.html', {'job':job_apply})

@login_required
def applications(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    applications = Application.objects.filter(user=user)
    return render(request, 'Jobs/applications.html', {'applications':applications})

@login_required
def application_detail(request, application_id):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    application = get_object_or_404(Application, pk=application_id)
    return render(request, 'Jobs/application_detail.html', {'application':application, 'user':user})

@user_passes_test(lambda u: u.is_superuser)
def allJobs(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    jobs = Job.objects.filter(user=user)
    return render(request, 'Jobs/employer_jobs_list.html', {'jobs':jobs})

@user_passes_test(lambda u: u.is_superuser)
def addJob(request):
    if request.method == "POST":
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        job = Job()
        job.user = user
        job.name = request.POST.get('name')
        job.description = request.POST.get('description')
        job.short_desc = request.POST.get('description')[:150]
        job.department = request.POST.get('department')
        job.deadline = request.POST.get('deadline')
        job.location = request.POST.get('location')
        if request.POST.get('international').lower() == "yes":
            job.international = True
        else:
            job.international = False
        job.eligibility = request.POST.get('eligibility')
        job.major = request.POST.get('major')
        # job.status = request.POST.get('status')
        job.save()
        return redirect('allJobs')
    return render(request, 'Jobs/create_job.html')

@user_passes_test(lambda u: u.is_superuser)
def removeJob(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    job.delete()
    return redirect('allJobs')

@user_passes_test(lambda u: u.is_superuser)
def editJob(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == "POST":
        job.name = request.POST.get('name')
        job.description = request.POST.get('description')
        job.short_desc = request.POST.get('description')[:150]
        job.department = request.POST.get('department')
        job.deadline = request.POST.get('deadline')
        job.location = request.POST.get('location')
        job.international = request.POST.get('international')
        job.eligibility = request.POST.get('eligibility')
        job.major = request.POST.get('major')
        # job.status = request.POST.get('status')
        job.save()
        return redirect('allJobs')
    return render(request, 'Jobs/editJob.html', {'job': job})

@user_passes_test(lambda u: u.is_superuser)
def applicantList(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    applications = Application.objects.filter(job=job)
    return render(request, 'Jobs/applicant_list.html', {'applications' : applications})

@user_passes_test(lambda u: u.is_superuser)
def applicationDetailEmployer(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    return render(request, 'Jobs/application_detail_employer.html', {'application':application})

@user_passes_test(lambda u: u.is_superuser)
def userDetail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'Jobs/user_detail.html',{'user':user})

@user_passes_test(lambda u: u.is_superuser)
def decisionDecline(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    if request.method == "POST":
        application.decision = "Rejected"
        application.save()
        return render(request, 'Jobs/application_detail_employer.html', {'application':application})
    return render(request, 'Jobs/application_detail_employer.html', {'application':application})

@user_passes_test(lambda u: u.is_superuser)
def decisionAccept(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    if request.method == "POST":
        application.decision = "Accepted"
        application.save()
        print(application.decision)
        return render(request, 'Jobs/application_detail_employer.html', {'application':application})
    return render(request, 'Jobs/application_detail_employer.html', {'application':application})