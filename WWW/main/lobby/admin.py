from django.contrib import admin
from lobby.models import *
from django.db import models
from django.contrib.auth.models import UserManager
from os import rename

import pprint

# Declaration des classes precisant l'affichage
class ProfilAdmin(admin.ModelAdmin):
   list_display   = ('username', 'status', 'role', 'description')

class ChallengeAdmin(admin.ModelAdmin):
    list_display   = ('name', 'creator', 'description', 'file', 'category', 'level', 'status','process','clue','token')
    actions = ['make_public']

    def make_public(self, request, queryset):

        #Changement de la du status en public
        queryset.update(status='public')
        '''
        #Deplacement du fichier
        for key in queryset.values_list('file'):
            filename=key
            self.message_user(request, "validated/public/docker/%s" % filename)
            queryset.update(status="validated/public/docker/%s" % filename)
            #os.rename("%s" %filename ,"/media/validated/public/docker/%s" % filename)

        #Deplacement du docker
        for key in queryset.values_list('file'):
            self.message_user(request, key)
            #os.rename("","/media/validated/")
        '''

    make_public.short_description = "Rendre publique"

class EventAdmin(admin.ModelAdmin):
   list_display   = ('name', 'description', 'place', 'training_event', 'date_start','date_end')

admin.site.register(Challenge,ChallengeAdmin)
admin.site.register(Profil, ProfilAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Event_Challenge)
admin.site.register(UEC)