from django.contrib import admin
from lobby.models import *

# Register your models here.
from django.db import models
from django.contrib.auth.models import UserManager


# Declaration des classes precisant l'affichage
class ProfilAdmin(admin.ModelAdmin):
   list_display   = ('username', 'status', 'role', 'description')

class ChallengesAdmin(admin.ModelAdmin):
   list_display   = ('name', 'creator', 'description', 'category', 'level', 'status','process','clue',)

class EventsAdmin(admin.ModelAdmin):
   list_display   = ('name', 'description', 'place', 'training_event', 'date_start','date_end')

admin.site.register(Challenges,ChallengesAdmin)
admin.site.register(Profil, ProfilAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(Event_Challenge)
admin.site.register(UEC)