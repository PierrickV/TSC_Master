from django.http import HttpResponse
from django.shortcuts import render

def profil(request):
	#Si il est connect
    #return render(request, 'lobby/home.html', locals())

    #Sinon...
    return render(request, 'profil/base.html', locals())

def myprofil(request):
	return render(request, 'profil/home.html', locals())
