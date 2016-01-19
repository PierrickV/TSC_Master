from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from lobby.views import *
from . import views

urlpatterns = patterns('lobby.views',
	url(r'^$', 'home'),
    url(r'connect/$', 'connect'),
    url(r'subscribe/$', 'subscribe'),
    url(r'disconnect/$', 'disconnect'),
    url(r'participate/(?P<id>[0-9]+)/$', 'participate_ev', name='participate-ev'),	
)

#urlpatterns = [
#    url(r'^', 'home'),
#    url(r'^home/', 'home'),
#]