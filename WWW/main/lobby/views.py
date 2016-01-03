from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from lobby.models import User



def home(request):
	if request.user.is_authenticated():
		return render(request, 'lobby/home.html', locals())
	else:	
		return render(request, 'lobby/base.html', locals())


def connect(request):
	username = request.POST.get('username')
	password = request.POST.get('password')

	user = authenticate(username=username, password=password)

	if user is not None:
		login(request, user)
		return render(request, 'lobby/home.html', {})
	else:
		return render(request, 'lobby/base.html', locals())


def disconnect(request):
	if request.user.is_authenticated():
		logout(request)
		return render(request, 'lobby/base.html', locals())
	else:
		return redirect('lobby/home.html', locals())


def subscribe(request):
	email = request.POST.get('email')
	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	newusername = request.POST.get('newusername')
	password = request.POST.get('password')
	password2 = request.POST.get('password2')
	description = request.POST.get('description')
	
	new_guy = User.objects.create_user(username=newusername, email=email, password=password)
	new_guy.firstname = 'firstname'
	new_guy.lastname = 'lastname'
	new_guy.status = '1'
	new_guy.role = '1'
	new_guy.score = '0'
	new_guy.avatar = ''
	new_guy.description = 'description'
	user.set_password(password)
	#registration date

	new_guy.save()

	user = authenticate(username=newusername, password=password)

	if user is not None:
		login(request, user)
		return render(request, 'lobby/home.html', {})
	else:
		return render(request, 'lobby/base.html', {})