from . import views
from django.conf.urls import url

app_name = 'jobs'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add', views.AddJobView.as_view(), name='add'),
]