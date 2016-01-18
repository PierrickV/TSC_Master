# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('creator', models.CharField(max_length=40)),
                ('description', models.TextField(null=True)),
                ('category', models.CharField(max_length=40)),
                ('level', models.PositiveSmallIntegerField()),
                ('status', models.CharField(max_length=40)),
                ('process', models.TextField(null=True)),
                ('clue', models.CharField(max_length=40)),
                ('type_upload', models.PositiveSmallIntegerField()),
                ('url', models.CharField(max_length=100, null=True)),
                ('file', models.FileField(null=True, upload_to=b'')),
                ('points', models.PositiveSmallIntegerField()),
                ('token', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(null=True)),
                ('place', models.CharField(max_length=40)),
                ('training_event', models.BooleanField()),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Event_Challenge',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('challenge_id', models.ForeignKey(to='lobby.Challenge')),
                ('event_id', models.ForeignKey(to='lobby.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=40, null=True)),
                ('firstname', models.CharField(max_length=40, null=True)),
                ('lastname', models.CharField(max_length=40, null=True)),
                ('status', models.PositiveSmallIntegerField()),
                ('role', models.CharField(max_length=40)),
                ('score', models.PositiveSmallIntegerField()),
                ('avatar', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UEC',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('status_challenge', models.BooleanField()),
                ('score_event', models.PositiveSmallIntegerField()),
                ('event_challenge_id', models.ForeignKey(to='lobby.Event_Challenge')),
                ('user_id', models.ForeignKey(to='lobby.Profil')),
            ],
        ),
    ]
