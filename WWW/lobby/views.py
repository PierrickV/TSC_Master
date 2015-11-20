from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'lobby/home.html', locals())

def subscribe(request):
	return render(request, 'subscribe/form.html', locals())
