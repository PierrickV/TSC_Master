from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from lobby.models import User


def home(request):
	return render(request, 'lobby/base.html', locals())


def connect(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)

	if user is not None:
		login(request, user)
		return render(request, 'lobby/home.html', locals())
	else:
		return render(request, 'lobby/base.html', locals())


def disconnect(request):
	if request.user.is_authenticated():
		logout(request)
		return render(request, 'lobby/base.html', locals())
	else:
		return redirect('/home', locals())


def subscribe(request):
	mail = request.POST.get('mail')
	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	newusername = request.POST.get('newusername')
	password = request.POST.get('password')
	password2 = request.POST.get('password2')
	description = request.POST.get('description')

	#User.objects.raw('INSERT INTO lobby_user (firstname, lastname, username, password, description) VALUES (firstname, lastname, newusername, password, description)')
	#user = lobby.objects.raw('firstname', 'lastname', 'username', 'password', 'mail', 'description')

	return render(request, 'lobby/base.html', locals())