from django.db import models
from django.contrib.auth.models import UserManager


# Create your models here.
class Profil(models.Model):
   #user_id ajoute automatiquement par Django
   id = models.AutoField(primary_key=True)
   username = models.CharField(max_length=40, null=True)
   firstname = models.CharField(max_length=40, null=True)
   lastname = models.CharField(max_length=40, null=True)
   status = models.PositiveSmallIntegerField()
   role = models.CharField(max_length=40)
   score = models.PositiveSmallIntegerField()
   avatar = models.CharField(max_length=100, null=True)
   description = models.TextField(null=True)

class Challenge(models.Model):
   #challenge_id ajoute automatiquement par Django
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=40)
   creator = models.CharField(max_length=40)
   description = models.TextField(null=True)
   category = models.CharField(max_length=40)
   level = models.PositiveSmallIntegerField()
   status = models.CharField(max_length=40)
   process = models.TextField(null=True)
   clue = models.CharField(max_length=40)
   type_upload = models.PositiveSmallIntegerField()
   url = models.CharField(max_length=100, null=True)
   token = models.CharField(max_length=40, null=True)
   file = models.FileField(null=True)
   points = models.PositiveSmallIntegerField()

class Event(models.Model):
   #event_id ajoute automatiquement par Django
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=40)
   description = models.TextField(null=True)
   place = models.CharField(max_length=40)
   training_event = models.BooleanField()
   date_start = models.DateField(auto_now_add=False, auto_now=False)
   date_end = models.DateField(auto_now_add=False, auto_now=False)

class Event_Challenge(models.Model):
   #event_challenge_id ajoute automatiquement par Django
   id = models.AutoField(primary_key=True)
   challenge_id = models.ForeignKey('Challenge')
   event_id = models.ForeignKey('Event')

class UEC(models.Model):
   id = models.AutoField(primary_key=True)
   user_id = models.ForeignKey('Profil')
   event_challenge_id = models.ForeignKey('Event_Challenge')
   status_challenge = models.BooleanField()
   score_event = models.PositiveSmallIntegerField()

'''
Rajout de la possibilite d'ajoute une categorie

class Challenge(models.Model):
   #challenge_id ajoute automatiquement par Django
   id =  models.AutoField(primary_key=True)
   name = models.CharField(max_length=40)
   description = models.CharField(max_length=40)
   image =
'''