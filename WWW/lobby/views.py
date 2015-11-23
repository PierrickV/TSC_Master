from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	#Si il est connect
    #return render(request, 'lobby/home.html', locals())

    #Sinon...
    return render(request, 'lobby/base.html', locals())
