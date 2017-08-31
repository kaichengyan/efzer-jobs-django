from django.contrib import admin

# Register your models here.
from jobs.models import JobInfo

admin.site.register(JobInfo)