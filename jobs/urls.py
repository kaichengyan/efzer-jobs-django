from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = 'jobs'

urlpatterns = [
    url(r'^$', views.JobListView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.JobDetailView.as_view(), name='detail'),
    url(r'^add/$', views.AddJobView.as_view(), name='add'),
    # url(r'^add\.do/$', views.add_job, name='action_add'),
    # url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateJobView.as_view(), name='update'),
    # url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteJobView.as_view(), name='delete'),
    # url(r'^login/$', auth_views.login, {'template_name': 'jobs/login.html'}, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
]