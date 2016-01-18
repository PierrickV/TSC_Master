from django.contrib import admin
from lobby.models import *
from django.db import models
from django.contrib.auth.models import UserManager

def make_validate(modeladmin, request, queryset):
    queryset.update(process='valide')
make_validate.short_description = "Valider le challenge"

def make_public(modeladmin, request, queryset):
    queryset.update(status='public')
make_public.short_description = "Rendre de challenge public"

# Declaration des classes precisant l'affichage
class ProfilAdmin(admin.ModelAdmin):
   list_display   = ('username', 'status', 'role', 'description')

class ChallengeAdmin(admin.ModelAdmin):
    list_display   = ('name', 'creator', 'description', 'file', 'category', 'level', 'status','process','clue','token')
    actions = [make_validate]

class EventAdmin(admin.ModelAdmin):
   list_display   = ('name', 'description', 'place', 'training_event', 'date_start','date_end')

admin.site.register(Challenge,ChallengeAdmin)
admin.site.register(Profil, ProfilAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Event_Challenge)
admin.site.register(UEC)