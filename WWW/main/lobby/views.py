from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from lobby.models import *
from django.db.models import Q

def home(request):
	if request.user.is_authenticated():
		#last = Event.objects.latest('id')
		#event = last_event.exclude(training_event=True)
		#event = Event.objects.filter(training_event=False)
		#event = event.latest('id')
		#event = Event.objects.get(id = last)
		event = Event.objects.filter(training_event=False).order_by('-id')[0]
		return render(request, 'lobby/home.html', locals())
	else:
		event = Event.objects.filter(training_event=False).order_by('-id')[0]
		return render(request, 'lobby/base.html', locals())


def connect(request):
	event = Event.objects.filter(training_event=False).order_by('-id')[0]

	username = request.POST.get('username')
	password = request.POST.get('password')

	user = authenticate(username=username, password=password)

	if user is not None:
		login(request, user)
		event = Event.objects.filter(training_event=False).order_by('-id')[0]
		return render(request, 'lobby/home.html', locals())
	else:
		event = Event.objects.filter(training_event=False).order_by('-id')[0]
		return render(request, 'lobby/base.html', locals())


def disconnect(request):
	if request.user.is_authenticated():
		logout(request)
		response = logout(request, next_page=reverse('app.home.views.home'))
		response.delete_cookie('sessionid')
		event = Event.objects.filter(training_event=False).order_by('-id')[0]
		return response
	else:
		event = Event.objects.filter(training_event=False).order_by('-id')[0]
		return render(request, 'lobby/home.html', locals())


def subscribe(request):
	email = request.POST.get('email')
	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	newusername = request.POST.get('newusername')
	password = request.POST.get('password')
	password2 = request.POST.get('password2')
	description = request.POST.get('description')
	
	new_user = User.objects.create_user(username=newusername, email=email, password=password)
	new_user.set_password(password)
	new_user.save()
	
	new_profil = Profil(username = newusername, firstname = firstname, lastname = lastname, status = '1', role = 'user', score = '0', avatar = '', description = description)
	new_profil.save()

	user = authenticate(username=newusername, password=password)

	if user is not None:
		login(request, user)
		event = Event.objects.filter(training_event=False).order_by('-id')[0]
		return render(request, 'lobby/home.html', locals())
	else:
		event = Event.objects.filter(training_event=False).order_by('-id')[0]
		return render(request, 'lobby/base.html', locals())

def participate_ev(request, id):
	if request.user.is_authenticated():
		username = request.user.username

		user_entry = Profil.objects.get(username= username)

		#participation = UE(user_id= user_entry.id, event_id= event.id)
		#participation.save()
		
		event = Event.objects.filter(training_event=False).order_by('-id')[0]
		return render(request, 'lobby/participate.html', locals())
	else:
		event = Event.objects.filter(training_event=False).order_by('-id')[0]
		return render(request, 'lobby/base.html', locals())
