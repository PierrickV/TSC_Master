# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0015_profil_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenges',
            name='file',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='challenges',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
