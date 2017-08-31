from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

from jobs.models import JobInfo


class IndexView(generic.ListView):
    template_name = 'jobs/index.html'
    context_object_name = 'job_list'

    def get_queryset(self):
        return JobInfo.objects.filter(published=True).order_by('-date_published')[:10]


class DetailView(generic.DetailView):
    model = JobInfo
    template_name = 'jobs/detail.html'


class AddJobView(generic.CreateView):
    model = JobInfo
    template_name = 'jobs/add.html'


def detail(request, pk):
    job = get_object_or_404(JobInfo, pk=pk)
    job.times_viewed += 1
    return render(request, 'jobs/detail.html', context={'jobinfo': job})