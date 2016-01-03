# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0011_auto_20160102_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='registration_date',
        ),
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date joined'),
        ),
    ]
