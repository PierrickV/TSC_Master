from django.contrib import admin
from lobby.models import *
from django.db import models
from django.contrib.auth.models import UserManager
import os

import pprint


public_file_path="validated/public/file/"
public_docker_path="validated/public/docker/"
private_file_path="validated/private/file/"
private_file_path= 'validated/private/docker/'

# Declaration des classes precisant l'affichage
class ProfilAdmin(admin.ModelAdmin):
   list_display   = ('username', 'status', 'role', 'description')

class ChallengeAdmin(admin.ModelAdmin):
    list_display   = ('name', 'creator', 'description', 'file', 'url', 'category', 'level', 'status','process','clue','token')
    actions = ['make_public','make_valide']

    #Changement du status en "public"
    def make_public(self, request, queryset):    #Rendre public
        queryset.update(status='public')
        #Deplacement du fichier
        for key in queryset.values_list('file'):
            src_path= ''.join(key) #tuple to string
            filename= os.path.basename(src_path)
            dst_path=public_file_path + "%s" % filename

            self.message_user(request,  "moving %s from %s to %s" % (filename,src_path,dst_path,))
            #os.rename(src_path ,dst_path)
            #queryset.update(file=dst_path)

    make_public.short_description = "Rendre publique"

    #Rendre public
    #Rendre prive
    #Valider et rendre public
    #Valider et rendre prive

    #Changement du process en "valide"
    def make_valide(self, request, queryset):

        #Changement du status en public
        queryset.update(process='valide')
    make_valide.short_description = "Valider"

class EventAdmin(admin.ModelAdmin):
   list_display   = ('name', 'description', 'place', 'training_event', 'date_start','date_end')

admin.site.register(Challenge,ChallengeAdmin)
admin.site.register(Profil, ProfilAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Event_Challenge)
admin.site.register(UEC)