# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0017_auto_20160111_1644'),
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
            ],
        ),
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.AlterField(
            model_name='event_challenge',
            name='challenge_id',
            field=models.ForeignKey(to='lobby.Challenge'),
        ),
        migrations.DeleteModel(
            name='Challenges',
        ),
    ]
