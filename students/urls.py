from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.student_homepage, name='student_homepage'),
    path('login', views.student_login, name='student_login'),
    path('register', views.student_register, name='student_register'),
    path('logout', views.student_logout, name='student_logout'),
    path('jobsposted', views.alljobs, name='alljobs'),
    path('employerHomepage/', views.employerHomepage, name='employerHomepage')
]