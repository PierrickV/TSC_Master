from django.http import HttpResponse
from django.shortcuts import render
from forms import ConnectForm

def home(request):
	form = ConnectForm()
	return render(request, 'lobby/base.html', locals())


def form(request):
	if request.method == 'GET':
		form = ConnectForm()
	else:
        # A Connect request: Handle Form Upload
		form = ConnectForm(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
		#if form.is_valid():
 
	return render(request, 'lobby/base.html', {
		'form': form,
    })