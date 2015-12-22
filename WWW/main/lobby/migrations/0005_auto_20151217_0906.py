# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0004_auto_20151217_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_challenge',
            name='challenge_id',
        ),
        migrations.RemoveField(
            model_name='event_challenge',
            name='event_id',
        ),
        migrations.RemoveField(
            model_name='uec',
            name='event_challenge_id',
        ),
        migrations.RemoveField(
            model_name='uec',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Challenges',
        ),
        migrations.DeleteModel(
            name='Event_Challenge',
        ),
        migrations.DeleteModel(
            name='Events',
        ),
        migrations.DeleteModel(
            name='UEC',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
