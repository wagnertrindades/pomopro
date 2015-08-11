from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Login
    url(r'^$', 'django.contrib.auth.views.login', 
        {'template_name' : 'accounts/home.html'}, name='home'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page' : 'accounts:home'}, name='logout'),
    url(r'^register/$', 'project.accounts.views.register', name='register'),
    url(r'^nova-senha/$', 'project.accounts.views.password_reset', name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)$', 
        'project.accounts.views.password_reset_confirm', name='password_reset_confirm'),
)