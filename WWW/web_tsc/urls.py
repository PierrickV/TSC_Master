#web_tsc URL Configuration

from django.conf.urls import include, url
from django.contrib import admin
from spirit.settings import *
from spirit.category import *

urlpatterns = [
	 url(r'^', include('spirit.urls', namespace="spirit", app_name="spirit")),
	 url(r'^$', include('lobby.urls')),
	 url(r'^home/', include('lobby.urls')),
	 url(r'^challenges/', include('challenges.urls')),
	 url(r'^profil/', include('profil.urls')),
     url(r'^', include('spirit.urls'))
]
