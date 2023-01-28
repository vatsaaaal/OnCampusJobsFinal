from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.models import User

from Jobs.models import Job

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

def student_homepage(request):
    return render(request, 'students/student_homepage.html')

def student_register(request):
    form = CreateUserForm()

    if request.method == "POST":
        if request.POST.get('employer'):
            user = User()
            user.username = request.POST.get('username')
            user.email = request.POST.get('email')
            user.set_password(request.POST.get('password1'))
            user.is_staff = True
            user.is_superuser = True
            user.save()
            return redirect('student_login')
        else:
            user = User()
            user.username = request.POST.get('username')
            user.email = request.POST.get('email')
            user.set_password(request.POST.get('password1'))
            user.save()
            return redirect('student_login')
    context = {'form':form}
    return render(request, 'students/student_register.html', context)

def student_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return render(request, 'students/employer_homepage.html')
        elif user is not None:
            login(request, user)
            return redirect('student_homepage')
        else:
            messages.info(request, 'Username or Password is Incorrect.')
    context = {}
    return render(request, 'students/student_login.html', context)

def student_logout(request):
    logout(request)
    return redirect('student_login')

def employerHomepage(request):
    return render(request, 'students/employer_homepage.html')

@login_required
def alljobs(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    jobs = Job.objects.filter(user=user)
    return render(request, 'students/posted_jobs.html', {'jobs':jobs})