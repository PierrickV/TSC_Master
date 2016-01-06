# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0013_auto_20160104_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='firstname',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='lastname',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
