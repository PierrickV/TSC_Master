from django.conf.urls import patterns, url

urlpatterns = patterns('lobby.views',
    url(r'', 'home'),
    url(r'^/accueil$', 'home')
)