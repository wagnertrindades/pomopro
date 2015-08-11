from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', 'project.core.views.timer', name='timer'),
)