from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.utils.translation import ugettext as _

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


class AddJobView(SuccessMessageMixin, generic.CreateView):
    model = Job
    form_class = JobForm
    success_url = reverse_lazy('jobs:index')
    success_message = _('申请已提交，审核后将发布到主页')


class UpdateJobView(generic.UpdateView):
    model = Job
    form_class = JobForm


class DeleteJobView(generic.DeleteView):
    model = Job
    success_url = reverse_lazy('jobs:index')