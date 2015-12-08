from django.conf.urls import patterns, url

urlpatterns = patterns('challenges.views',
	url(r'^$', 'home'),
    url(r'post/$', 'post'),
    url(r'web/$', 'web'),
    url(r'realist/$', 'realist'),
    url(r'reverse/$', 'reverse'),
    url(r'application/$', 'application'),
    url(r'network/$', 'network'),
    url(r'programming/$', 'programming'),
    url(r'forensic/$', 'forensic'),
    url(r'steganography/$', 'steganography')
)