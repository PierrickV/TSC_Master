# -*- coding: utf-8 -*-

# MINIMAL CONFIGURATION FOR PRODUCTION ENV

# Create your own prod_local.py
# import * this module there and use it like this:
# python manage.py runserver --settings=project.settings.prod_local

from __future__ import unicode_literals

from .base import *


DEBUG = False

# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    (u'Alan Barth', 'alan.barthelemy@gmail.com'),
    (u'Pierrick Veran', 'veran@intechinfo.fr')
)
# Secret key generator: https://djskgen.herokuapp.com/
# You should set your key as an environ variable
SECRET_KEY = os.environ.get("SECRET_KEY", "jlgnu0x7=axt@$de)wr$-(8(wru3)ra-b&*39trov9mt50@1@c")

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    '.tsc.itinet.fr',  # Allow domain and subdomains
]
# Database
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'tsc_database',  # Nom de la base de données
		'USER': 'django',            # Utilisateur
		'PASSWORD': 'django',        # Mot de passe si nécessaire
		'HOST': 'tsc_database',         # Utile si votre base de données est sur une autre machine
		'PORT': '3306',                  # ... et si elle utilise un autre port que celui par défaut
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreply.tsc@gmail.com'
EMAIL_HOST_PASSWORD = '7486bc89c753eabe273d6063d174f97d'
