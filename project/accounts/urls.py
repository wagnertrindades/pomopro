from django.conf.urls import patterns, include, url

urlpatterns = patterns('project.accounts.views',
    url(r'^$', 'home', name='home'),
)