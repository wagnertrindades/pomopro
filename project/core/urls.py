from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Login
    url(r'^$', 'django.contrib.auth.views.login', 
        {'template_name' : 'home.html'}, name='home'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page' : 'core:home'}, name='logout'),
    url(r'^register/$', 'project.core.views.register', name='register'),
    # url(r'^nova-senha/$', 'project.core.views.password_reset', name='password_reset'),
    url(r'^timer/$', 'project.core.views.timer', name='timer'),
)