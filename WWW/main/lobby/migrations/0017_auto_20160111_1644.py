# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0016_auto_20160104_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='date_start',
            field=models.DateField(),
        ),
    ]
