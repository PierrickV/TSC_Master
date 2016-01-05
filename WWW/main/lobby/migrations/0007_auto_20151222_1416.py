# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0006_auto_20151217_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
                ('role', models.CharField(max_length=40)),
                ('score', models.PositiveSmallIntegerField()),
                ('avatar', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='challenges',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='event_challenge',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='uec',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='uec',
            name='user_id',
            field=models.ForeignKey(to='lobby.User'),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
