from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from challenges.views import *
from . import views

urlpatterns = patterns('challenges.views',
	url(r'^$', 'home'),
    url(r'post/$', 'post'),
    url(r'add/$', 'add'),
    url(r'web/$', 'web'),
    url(r'web/(?P<id>[0-9]+)/$', 'web_ep', name='web-ep'),
    url(r'realist/$', 'realist'),
    url(r'realist/(?P<id>[0-9]+)/$', 'realist_ep', name='realist-ep'),
    url(r'reverse/$', 'reverse'),
    url(r'reverse/(?P<id>[0-9]+)/$', 'reverse_ep', name='reverse-ep'),
    url(r'application/$', 'application'),
    url(r'application/(?P<id>[0-9]+)/$', 'application_ep', name='application-ep'),
    url(r'network/$', 'network'),
    url(r'network/(?P<id>[0-9]+)/$', 'network_ep', name='network-ep'),
    url(r'programming/$', 'programming'),
    url(r'programming/(?P<id>[0-9]+)/$', 'programming_ep', name='programming-ep'),
    url(r'forensic/$', 'forensic'),
    url(r'forensic/(?P<id>[0-9]+)/$', 'forensic_ep', name='forensic-ep'),
    url(r'steganography/$', 'steganography'),
    url(r'steganography/(?P<id>[0-9]+)/$', 'steganography_ep', name='staganography-ep'),
    url(r'valid/$', 'valid'),
)

#urlpatterns = [
#    url(r'^$', 'home'),
#    url(r'post/$', 'post'),
#    url(r'web/$', 'web'),
#    url(r'realist/$', 'realist'),
#    url(r'reverse/$', 'reverse'),
#    url(r'application/$', 'application'),
#    url(r'network/$', 'network'),
#    url(r'programming/$', 'programming'),
#    url(r'forensic/$', 'forensic'),
#    url(r'steganography/$', 'steganography')
#]