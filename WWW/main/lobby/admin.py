from django.contrib import admin
from lobby.models import *
from django.db import models
from django.contrib.auth.models import UserManager
import os

public_file_path = "./validated/public/file/"
private_file_path = "./validated/private/file/"

public_docker_path = "./validated/public/docker/"
private_docker_path = './validated/private/docker/'


# Declaration des classes precisant l'affichage
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('username', 'status', 'role', 'description')


class ChallengeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'creator', 'description', 'file', 'url', 'category', 'level', 'status', 'process', 'clue', 'token')
    actions = ['make_valid_public', 'make_valid_private', 'make_public', 'make_private']

    # Valider et rendre public
    def make_valid_public(self, request, queryset):
        queryset.update(status='public')
        queryset.update(process='valide')
        # Deplacement du fichier
        '''for key in queryset.values_list('file'):
            src_path = ''.join(key)  # tuple to string
            filename = os.path.basename(src_path)
            dst_path = public_file_path + "%s" % filename

            self.message_user(request, "moving %s from %s to %s" % (filename, src_path, dst_path,))
            os.rename(src_path, dst_path)
            queryset.update(file=dst_path)'''

    make_valid_public.short_description = "Valider et rendre publique"

    # Valider et rendre prive
    def make_valid_private(self, request, queryset):
        queryset.update(status='private')
        queryset.update(process='valide')
        # Deplacement du fichier
        '''for key in queryset.values_list('file'):
            src_path = ''.join(key)  # tuple to string
            filename = os.path.basename(src_path)
            dst_path = private_file_path + "%s" % filename

            self.message_user(request, "moving %s from %s to %s" % (filename, src_path, dst_path,))
            os.rename(src_path, dst_path)'''

    make_valid_private.short_description = "Valider et rendre secret"

    # Rendre prive
    def make_private(self, request, queryset):
        queryset.update(status='private')
        # Deplacement du fichier


        '''for key in queryset.values_list('file'):
            src_path = ''.join(key)  # tuple to string
            filename = os.path.basename(src_path)
            dst_path = public_file_path + "%s" % filename

            self.message_user(request, "moving %s from %s to %s" % (filename, src_path, dst_path,))
            os.rename(src_path, dst_path)
            queryset.update(file=dst_path)'''


    make_private.short_description = "Rendre secret"


    # Rendre public
    def make_public(self, request, queryset):
        queryset.update(status='public')
        # Deplacement du fichier
        '''for key in queryset.values_list('file'):
            src_path = ''.join(key)  # tuple to string
            filename = os.path.basename(src_path)
            dst_path = public_file_path + "%s" % filename

            self.message_user(request, "moving %s from %s to %s" % (filename, src_path, dst_path,))
            os.rename(src_path, dst_path)
            queryset.update(file=dst_path)'''


    make_public.short_description = "Rendre public"


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'place', 'training_event', 'date_start', 'date_end')


admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Profil, ProfilAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Event_Challenge)
admin.site.register(UEC)
