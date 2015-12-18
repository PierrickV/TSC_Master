# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0002_auto_20151214_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('creator', models.CharField(max_length=40)),
                ('description', models.TextField(null=True)),
                ('category', models.CharField(max_length=40)),
                ('level', models.PositiveSmallIntegerField()),
                ('status', models.CharField(max_length=40)),
                ('process', models.TextField(null=True)),
                ('clue', models.CharField(max_length=40)),
                ('type_upload', models.PositiveSmallIntegerField()),
                ('url', models.CharField(max_length=100)),
                ('points', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event_Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('challenge_id', models.ForeignKey(to='lobby.Challenges')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(null=True)),
                ('place', models.CharField(max_length=40)),
                ('training_event', models.BooleanField()),
                ('date_start', models.DateField(auto_now_add=True)),
                ('date_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UEC',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('status_challenge', models.BooleanField()),
                ('score_event', models.PositiveSmallIntegerField()),
                ('event_challenge_id', models.ForeignKey(to='lobby.Event_Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
                ('role', models.CharField(max_length=40)),
                ('score', models.PositiveSmallIntegerField()),
                ('avatar', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='uec',
            name='user_id',
            field=models.ForeignKey(to='lobby.Users'),
        ),
        migrations.AddField(
            model_name='event_challenge',
            name='event_id',
            field=models.ForeignKey(to='lobby.Events'),
        ),
    ]
