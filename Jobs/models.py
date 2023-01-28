from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    department = models.CharField(max_length=100, blank = True)
    deadline = models.DateField()
    location = models.CharField(max_length=100)
    international = models.BooleanField()
    eligibility = models.TextField()
    major = models.CharField(max_length=100, blank = True)
    status = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.name

class Application(models.Model):
    job = models.ForeignKey("Job", on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)
    email = models.EmailField()
    major = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    fit = models.TextField()
    resume = models.FileField(upload_to='resume/', max_length=100, blank=True)
    decision = models.CharField(max_length=100, default='Pending')

    def __str__(self):
        return str(self.job) + " : " + str(self.user)