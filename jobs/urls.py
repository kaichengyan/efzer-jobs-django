from . import views
from django.conf.urls import url

app_name = 'jobs'

urlpatterns = [
    url(r'^$', views.JobListView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add/$', views.AddJobView.as_view(), name='add'),
    url(r'^add\.do/$', views.add_job, name='action_add'),
]