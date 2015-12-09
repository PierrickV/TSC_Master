from django.http import HttpResponse
from django.shortcuts import render

def profil(request):
    return render(request, 'profil/base.html', locals())

def myprofil(request):
	#Si il est pas connect
    #return render(request, 'lobby/home.html', locals())

    #Sinon...
	return render(request, 'profil/myprofil.html', locals())
