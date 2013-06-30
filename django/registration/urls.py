from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^signup/$', 'registration.views.signup', name='signup'),
	# Examples:
	# url(r'^$', 'assassin.views.home', name='home'),
	# url(r'^assassin/', include('assassin.foo.urls')),
)