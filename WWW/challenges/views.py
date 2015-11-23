from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'challenges/home.html', locals())

def web(request):
	return render(request, 'challenges/web.html', locals())