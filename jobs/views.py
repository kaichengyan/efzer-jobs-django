from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import generic

from jobs.models import JobInfo


class JobListView(generic.ListView):
    template_name = 'jobs/index.html'
    context_object_name = 'job_list'

    def get_queryset(self):
        return JobInfo.objects.filter(published__exact=True).order_by('-date_published')[:10]


class DetailView(generic.DetailView):
    model = JobInfo
    template_name = 'jobs/detail.html'

    def get_queryset(self):
        return JobInfo.objects.filter(published__exact=True)


class AddJobView(generic.CreateView):
    model = JobInfo
    template_name = 'jobs/add.html'
    fields = ['company']


# def detail(request, pk):
#     job = get_object_or_404(JobInfo, pk=pk)
#     job.times_viewed += 1
#     return render(request, 'jobs/detail.html', context={'jobinfo': job})

def add_job(request):
    try:
        company = request.POST['company']
        location = request.POST['location']
        job_position = request.POST['job_position']
        department = request.POST['department']
        publisher = request.POST['publisher']
        description = request.POST['description']
        requirements = request.POST['requirements']
        submitting_resume = request.POST['submitting_resume']
        company_description = request.POST['company_description']
    except KeyError:
        return HttpResponse('Error')
    else:
        job = JobInfo.objects.create(
            company=company,
            location=location,
            job_position=job_position,
            department=department,
            publisher=publisher,
            description=description,
            requirements=requirements,
            submitting_resume=submitting_resume,
            company_description=company_description,
        )
        job.save()
        return HttpResponseRedirect(reverse('jobs:index'))
