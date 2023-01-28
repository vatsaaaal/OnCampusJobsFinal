import django_filters
from django_filters import DateFilter

from .models import Job

set_dept = []
set_major = []
job = Job.objects.all()
for i in job:
    set_dept += [(i.department, i.department)]
    set_major += [(i.major, i.major)]
set_dept = tuple(set_dept)
set_major = tuple(set_major)

LOC_CHOICES = (
    ('University City Campus', 'University City Campus'),
    ('Centre City Campus','Centre City Campus'),
    ('Queen Lane Campus','Queen Lane Campus'),
    ('Academy of Natural Sciences','Academy of Natural Sciences'),
    ('LeBow College of Business Malvern Campus','LeBow College of Business Malvern Campus')
)

ELG_CHOICES = (
    ('Freshmen','Freshmen'),
    ('Sophomore','Sophomore'),
    ('Pre-Junior','Pre-Junior'),
    ('Junior','Junior'),
    ('Senior','Senior'),
)

class JobFilter(django_filters.FilterSet):
    location = django_filters.ChoiceFilter(choices=LOC_CHOICES)
    department = django_filters.ChoiceFilter(choices=set_dept)
    eligibility = django_filters.ChoiceFilter(choices=ELG_CHOICES)
    major = django_filters.ChoiceFilter(choices=set_major)
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['name', 'short_desc', 'description', 'deadline', 'status', 'flex_time']


