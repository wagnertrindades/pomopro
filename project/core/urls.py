from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Login
    url(r'^$', 'django.contrib.auth.views.login', 
        {'template_name' : 'home.html'}, name='home'),
    # Logout
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page' : 'core:home'}, name='logout'),
    url(r'^timer/$', 'project.core.views.timer', name='timer'),
)