from django.conf.urls import patterns, url

urlpatterns = patterns('challenges.views',
	url(r'', 'home'),
    url(r'^challenges/$', 'home'),
    url(r'^challenges/web/$', 'web')
)