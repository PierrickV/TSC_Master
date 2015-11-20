from django.http import HttpResponse
from django.shortcuts import render


def form(request):
    return render(request, 'post_challenge/form.html', locals())
