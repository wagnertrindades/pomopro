from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', 
        {'template_name' : 'home.html'}, name='home'),
    url(r'^timer/$', 'project.core.timer', name='timer'),
)