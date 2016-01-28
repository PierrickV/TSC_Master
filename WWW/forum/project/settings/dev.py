# -*- coding: utf-8 -*-

# THIS IS FOR DEVELOPMENT ENVIRONMENT
# DO NOT USE IT IN PRODUCTION

# Create your own dev_local.py
# import * this module there and use it like this:
# python manage.py runserver --settings=project.settings.dev_local

from __future__ import unicode_literals

from .base import *


DEBUG = False

TEMPLATES[0]['OPTIONS']['debug'] = False
# TEMPLATES[0]['OPTIONS']['string_if_invalid'] = '{{ %s }}'  # Some Django templates relies on this being the default

ADMINS = (( 'veran@intechinfo.fr'), )  # Log email to console when DEBUG = False

SECRET_KEY = "DEV"

ALLOWED_HOSTS = [
    '.tsc.itinet.fr',  # Allow domain and subdomains
]

# INSTALLED_APPS.extend([
#    'debug_toolbar',
# ])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES.update({
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
})

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
