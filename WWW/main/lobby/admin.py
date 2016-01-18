from django.contrib import admin
from lobby.models import *

# Register your models here.
from django.db import models
from django.contrib.auth.models import UserManager


# Declaration des classes precisant l'affichage
class ProfilAdmin(admin.ModelAdmin):
   list_display   = ('username', 'status', 'role', 'description')

class ChallengeAdmin(admin.ModelAdmin):
   list_display   = ('name', 'creator', 'description', 'file', 'category', 'level', 'status','process','clue','token')

class EventAdmin(admin.ModelAdmin):
   list_display   = ('name', 'description', 'place', 'training_event', 'date_start','date_end')

admin.site.register(Challenge,ChallengeAdmin)
admin.site.register(Profil, ProfilAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Event_Challenge)
admin.site.register(UEC)