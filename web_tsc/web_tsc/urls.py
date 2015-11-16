#web_tsc URL Configuration

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	 url(r'', include('lobby.urls')),
	 url(r'^/home', include('lobby.urls'))
]
