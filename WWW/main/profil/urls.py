from django.conf.urls import patterns, url

urlpatterns = patterns('profil.views',
	url(r'^$', 'profil'),
    url(r'my/$', 'myprofil'),
)

#urlpatterns = [
#    url(r'^$', 'profil'),
#    url(r'my/$', 'myprofil'),
#]