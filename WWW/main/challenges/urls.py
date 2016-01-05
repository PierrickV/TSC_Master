from django.conf.urls import patterns, url

urlpatterns = patterns('challenges.views',
	url(r'^$', 'home'),
    url(r'post/$', 'post'),
    url(r'web/$', 'web'),
    url(r'web/([0-9]{3})/$', 'web_ep'),
    url(r'realist/$', 'realist'),
    url(r'realist/([0-9]{3})/$', 'realist_ep'),
    url(r'reverse/$', 'reverse'),
    url(r'reverse/([0-9]{3})/$', 'reverse_ep'),
    url(r'application/$', 'application'),
    url(r'application/([0-9]{3})/$', 'application_ep'),
    url(r'network/$', 'network'),
    url(r'network/([0-9]{3})/$', 'network_ep'),
    url(r'programming/$', 'programming'),
    url(r'programming/([0-9]{3})/$', 'programming_ep'),
    url(r'forensic/$', 'forensic'),
    url(r'forensic/([0-9]{3})/$', 'forensic_ep'),
    url(r'steganography/$', 'steganography'),
    url(r'steganography/([0-9]{3})/$', 'steganography_ep')
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