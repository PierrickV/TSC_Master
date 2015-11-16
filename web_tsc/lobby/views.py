from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    text = """<h1>Bienvenue sur ma page d'accueil !</h1>
              <p>Ca marche plutot bien !</p>"""
    return HttpResponse(text)