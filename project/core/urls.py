from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Login
    url(r'^$', 'django.contrib.auth.views.login', 
        {'template_name' : 'home.html'}, name='home'),
    # Logout
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page' : 'core:home'}, name='logout'),
    #Register
    url(r'^$', 'project.core.views.register', name='register'),
    url(r'^timer/$', 'project.core.views.timer', name='timer'),
)