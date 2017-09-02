from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import generic

from jobs.forms import JobForm
from jobs.models import Job


class JobListView(generic.ListView):
    template_name = 'jobs/index.html'
    context_object_name = 'job_list'

    def get_queryset(self):
        return Job.objects.filter(published=True).order_by('-date_published')


class JobDetailView(generic.DetailView):
    model = Job
    template_name = 'jobs/detail.html'
    queryset = Job.objects.filter(published=True)

    def get_queryset(self):
        return Job.objects.filter(published=True)

    def get_object(self, queryset=queryset):
        job = super(JobDetailView, self).get_object()
        job.times_viewed += 1
        job.save()
        return job


class AddJobView(generic.CreateView):
    model = Job
    form_class = JobForm
    success_url = reverse_lazy('jobs:index')


class UpdateJobView(generic.UpdateView):
    model = Job
    form_class = JobForm


class DeleteJobView(generic.DeleteView):
    model = Job
    success_url = reverse_lazy('jobs:index')


# def detail(request, pk):
#     job = get_object_or_404(JobInfo, pk=pk)
#     job.times_viewed += 1
#     return render(request, 'jobs/detail.html', context={'jobinfo': job})

# def add_job(request):
#     try:
#         company = request.POST['company']
#         location = request.POST['location']
#         job_position = request.POST['job_position']
#         department = request.POST['department']
#         publisher = request.POST['publisher']
#         description = request.POST['description']
#         requirements = request.POST['requirements']
#         submitting_resume = request.POST['submitting_resume']
#         company_description = request.POST['company_description']
#     except KeyError:
#         return HttpResponse('Error')
#     else:
#         job = Job.objects.create(
#             company=company,
#             location=location,
#             job_position=job_position,
#             department=department,
#             publisher=publisher,
#             description=description,
#             requirements=requirements,
#             submitting_resume=submitting_resume,
#             company_description=company_description,
#         )
#         job.save()
#         return HttpResponseRedirect(reverse('jobs:index'))
