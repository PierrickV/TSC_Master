# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0012_auto_20160103_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('status', models.PositiveSmallIntegerField()),
                ('role', models.CharField(max_length=40)),
                ('score', models.PositiveSmallIntegerField()),
                ('avatar', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='uec',
            name='user_id',
            field=models.ForeignKey(to='lobby.Profil'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
