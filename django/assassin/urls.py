from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin, auth
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'assassin.views.home', name='home'),
	# url(r'^assassin/', include('assassin.foo.urls')),

	url(r'^$', 'main.views.index'),

	(r'^accounts/', include('allauth.urls')),

	url(r'^games/', include('games.urls')),
	url(r'^game/(?P<id_number>\d+)/', include('gameplay.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	(r'^avatar/', include('avatar.urls')),
)


