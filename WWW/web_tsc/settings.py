# -*- coding: utf-8 -*-
#Django settings for web_tsc project.

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jlgnu0x7=axt@$de)wr$-(8(wru3)ra-b&*39trov9mt50@1@c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Un tuple qui énumère les personnes qui reçoivent les notifications d’erreurs dans le code
ADMINS = (
    (u'Alan Barth', 'alan.barthelemy@gmail.com'),
    (u'Pierrick Veran', 'veran@intechinfo.fr')
)

# Représente des noms de domaine/d’hôte que Django peut servir
ALLOWED_HOSTS = [
    '.tsc.itinet.fr',  # Allow domain and subdomains
]

# Database
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'tsc_database',  # Nom de la base de données
#        'USER': '<root>',            # Utilisateur
#        'PASSWORD': '<zIDCUiY55YwBOkQKbML2>',        # Mot de passe si nécessaire
#        'HOST': '127.0.0.1',         # Utile si votre base de données est sur une autre machine
#        'PORT': '3306',                  # ... et si elle utilise un autre port que celui par défaut
#    }}

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lobby',
    'post_challenge',
    'challenges'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'web_tsc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_ROOT = '/static/'

# Internationalization

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

WSGI_APPLICATION = 'web_tsc.wsgi.application'
