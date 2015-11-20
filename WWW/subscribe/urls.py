from django.conf.urls import patterns, url

urlpatterns = patterns('subscribe.views',
	url(r'','form'),
    url(r'subscribe/', 'form'),
)