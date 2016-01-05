from django.db import models
from django.contrib.auth.models import UserManager
from django.utils import timezone
import datetime


# Create your models here.
class User(models.Model):
   #user_id ajoute automatiquement par Django
   id = models.AutoField(primary_key=True)
   firstname = models.CharField(max_length=40)
   lastname = models.CharField(max_length=40)
   username = models.CharField(max_length=40)
   password = models.CharField(max_length=100)
   email = models.CharField(max_length=100)
   status = models.PositiveSmallIntegerField()
   role = models.CharField(max_length=40)
   score = models.PositiveSmallIntegerField()
   avatar = models.CharField(max_length=100, null=True)
   description = models.TextField(null=True)
   date_joined = models.DateTimeField(('date joined'), default=timezone.now)
   is_active = models.BooleanField(default=True)
   is_admin = models.BooleanField(default=False)
   is_staff = models.BooleanField(default=False)
   is_superuser = models.BooleanField(default=False)
   objects = UserManager()

class Challenges(models.Model):
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
   url = models.CharField(max_length=100)
   points = models.PositiveSmallIntegerField()

class Events(models.Model):
   #event_id ajoute automatiquement par Django
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=40)
   description = models.TextField(null=True)
   place = models.CharField(max_length=40)
   training_event = models.BooleanField()
   date_start = models.DateField(auto_now_add=True, auto_now=False)
   date_end = models.DateField(auto_now_add=False, auto_now=False)

class Event_Challenge(models.Model):
   #event_challenge_id ajoute automatiquement par Django
   id = models.AutoField(primary_key=True)
   challenge_id = models.ForeignKey('Challenges')
   event_id = models.ForeignKey('Events')

class UEC(models.Model):
   id = models.AutoField(primary_key=True)
   user_id = models.ForeignKey('User')
   event_challenge_id = models.ForeignKey('Event_Challenge')
   status_challenge = models.BooleanField()
   score_event = models.PositiveSmallIntegerField()
