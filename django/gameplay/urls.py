from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'gameplay.views.index', name='index'),
	url(r'^request-invite/$', 'gameplay.views.request_invite', name='invite'),
)