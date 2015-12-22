from django.conf.urls import patterns, url

urlpatterns = patterns('lobby.views',
	url(r'^$', 'home'),
    url(r'^form/$', 'form'),
    url(r'^validfc/$', 'validfc'),
    url(r'^validfs/$', 'validfs')
)

#urlpatterns = [
#    url(r'^', 'home'),
#    url(r'^home/', 'home'),
#]