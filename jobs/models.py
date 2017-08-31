from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class JobInfo(models.Model):
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    job_position = models.CharField(max_length=50, default="Employee")
    department = models.CharField(max_length=50, default="Default")
    date_published = models.DateTimeField(default=timezone.now)
    times_viewed = models.IntegerField(default=0)
    publisher = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    requirements = models.CharField(max_length=300)
    submitting_resume = models.CharField(max_length=300)
    company_description = models.CharField(max_length=2000)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.job_position + " at " + self.department + ", " + self.company
