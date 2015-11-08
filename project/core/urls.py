from django.conf.urls import patterns, include, url

urlpatterns = patterns('project.core.views',
    url(r'^', 'timer', name='timer'),
    url(r'^add-timer/(?P<status>\d+)/$', 'add_timer', name='add_timer'),
)