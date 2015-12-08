from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'challenges/home.html', locals())

def post(request):
    return render(request, 'challenges/post.html', locals())

def web(request):
	return render(request, 'challenges/web.html', locals())

def network(request):
	return render(request, 'challenges/network.html', locals())

def programming(request):
	return render(request, 'challenges/programming.html', locals())

def realist(request):
	return render(request, 'challenges/realist.html', locals())

def reverse(request):
	return render(request, 'challenges/reverse.html', locals())

def steganography(request):
	return render(request, 'challenges/steganography.html', locals())

def forensic(request):
	return render(request, 'challenges/forensic.html', locals())

def application(request):
	return render(request, 'challenges/application.html', locals())