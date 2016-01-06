from django.http import HttpResponse
from django.shortcuts import render
from lobby.models import *

def profil(request):
	username = user_active.username
	user_active = Profil.objects.get(username = username)

	
	return render(request, 'profil/base.html', locals())

def myprofil(request):
	if request.user.is_authenticated():
		username = request.user.username
		user_active = Profil.objects.get(username = username)
		date = request.user.date_joined
		description = user_active.description
		firstname = user_active.firstname
		lastname = user_active.lastname
		email = request.user.email

		return render(request, 'profil/myprofil.html', {'username': username, 'date': date, 'description': description, 'firstname': firstname, 'lastname': lastname, 'email': email})
	else:
		return render(request, 'lobby/base.html', locals())
