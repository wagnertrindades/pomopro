from django.conf.urls import patterns, include, url

urlpatterns = patterns('project.core.views',
    url(r'^$', 'home', name='home'),
)