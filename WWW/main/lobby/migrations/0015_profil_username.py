# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0014_auto_20160104_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='username',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
