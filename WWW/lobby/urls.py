from django.conf.urls import patterns, url

urlpatterns = patterns('lobby.views',
	url(r'^', 'home'),
    url(r'^home/$', 'home')
    url(r'^form/$', 'form')
)

#urlpatterns = [
#    url(r'^', 'home'),
#    url(r'^home/', 'home'),
#]