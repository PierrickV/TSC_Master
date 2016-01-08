from django.conf.urls import patterns, url

urlpatterns = patterns('lobby.views',
	url(r'^$', 'home'),
    url(r'connect/$', 'connect'),
    url(r'subscribe/$', 'subscribe'),
    url(r'disconnect/$', 'disconnect'),
    url(r'event_form/$', 'eventform'),
    url(r'participate/$', 'participate')
)

#urlpatterns = [
#    url(r'^', 'home'),
#    url(r'^home/', 'home'),
#]