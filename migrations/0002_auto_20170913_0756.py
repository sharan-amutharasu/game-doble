# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-13 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_dob2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mt_game',
            name='f_p1_started',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mt_game',
            name='f_p2_started',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mt_game',
            name='f_p3_started',
            field=models.IntegerField(default=0),
        ),
    ]
