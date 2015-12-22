# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0003_auto_20151214_0945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenges',
            old_name='category',
            new_name='challenges_category',
        ),
    ]
