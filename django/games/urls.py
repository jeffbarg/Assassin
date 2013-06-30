from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	# Examples:
	url(r'^$', 'games.views.index', name='games-index'),
	url(r'^new/$', 'games.views.new', name='games-new'),
	url(r'^edit/(?P<id_number>[\d]+)$', 'games.views.edit', name='games-edit'),
	url(r'^delete/(?P<id_number>[\d]+)$', 'games.views.delete', name='games-delete'),
	# url(r'^assassin/', include('assassin.foo.urls')),
)