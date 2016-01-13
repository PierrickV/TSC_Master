from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from lobby.models import *
import shutil

def home(request):
    return render(request, 'challenges/home.html', locals())

def post(request):
	if request.user.is_authenticated():
		return render(request, 'challenges/post.html', locals())
	else:
		return render(request, 'lobby/base.html', locals())

def add(request):
	if request.user.is_authenticated():
		username = request.user.username
		category = request.POST.get('category')

		name = request.POST.get('name')
		#name = name.replace(" ", "_")


		difficulty = request.POST.get('difficulty')
		typeadd = request.POST.get('typeadd')
		description = request.POST.get('description') 
		indice = request.POST.get('indice')
		solution = request.POST.get('solution')

		if typeadd == 'url':
			typeadd = '1'
			challenge = request.POST.get('challenge')
			new_challenge = Challenges(name = name, creator = username, description = description, category = category, level = difficulty, type_upload = typeadd, status = 'prive', process = 'non_valide', clue = indice, url = challenge, points = '10')
			new_challenge.save()
		elif typeadd == 'zip':
			typeadd = '2'
			fichier = request.FILES['challenge']
			fichier.name = name.replace(" ", "_") + '.zip'
			url = 'dl.tsc.itinet.fr/' + category + '/' + fichier.name + '/'

			new_challenge = Challenges(name = name, creator = username, description = description, category = category, level = difficulty, type_upload = typeadd, status = 'prive', process = 'non_valide', clue = indice, file = fichier, url = url, points = '10')
			new_challenge.save()
		else:
			typeadd = '3'


		return render(request, 'challenges/home.html', locals())
	else:
		return render(request, 'lobby/base.html', locals())


def web(request):
	challenges = Challenges.objects.filter(category = 'Web')
	#challenges = challenges.order_by('level')
	for key in challenges:
		challenges.name = challenges.name.replace("_", " ")
	
	return render(request, 'challenges/web.html', locals())

def web_ep(request, id):
	epreuve = Challenges.objects.get(id = id)
	epreuve.name = epreuve.name.replace("_", " ")

	return render(request, 'challenges/ep.html', locals())

def network(request):
	challenges = Challenges.objects.filter(category = 'Network')
	return render(request, 'challenges/network.html', locals())

def network_ep(request):
	return render(request, 'challenges/ep.html', locals())

def programming(request):
	challenges = Challenges.objects.filter(category = 'Programming')
	return render(request, 'challenges/programming.html', locals())

def programming_ep(request):
	return render(request, 'challenges/web.html', locals())

def realist(request):
	challenges = Challenges.objects.filter(category = 'Realist')
	return render(request, 'challenges/realist.html', locals())

def realist_ep(request):
	return render(request, 'challenges/web.html', locals())

def reverse(request):
	challenges = Challenges.objects.filter(category = 'Reverse')
	return render(request, 'challenges/reverse.html', locals())

def reverse_ep(request):
	return render(request, 'challenges/web.html', locals())

def steganography(request):
	challenges = Challenges.objects.filter(category = 'Steganography')
	return render(request, 'challenges/steganography.html', locals())

def steganography_ep(request):
	return render(request, 'challenges/web.html', locals())

def forensic(request):
	challenges = Challenges.objects.filter(category = 'Forensic')
	return render(request, 'challenges/forensic.html', locals())

def forensic_ep(request):
	return render(request, 'challenges/web.html', locals())

def application(request):
	challenges = Challenges.objects.filter(category = 'Application')
	return render(request, 'challenges/application.html', locals())

def application_ep(request):
	return render(request, 'challenges/web.html', locals())
