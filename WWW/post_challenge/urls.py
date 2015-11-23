from django.conf.urls import patterns, url

urlpatterns = patterns('post_challenge.views',
	url(r'', 'form'),
    url(r'^post_challenge/$', 'form'),
)