from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	# Examples:
	url(r'^$', 'games.views.index', name='index'),
	url(r'^new/$', 'games.views.new', name='new'),
	url(r'^edit/(?P<id_number>[\d]+)$', 'games.views.edit', name='edit'),
	url(r'^delete/(?P<id_number>[\d]+)$', 'games.views.delete', name='delete'),
	# url(r'^assassin/', include('assassin.foo.urls')),
)