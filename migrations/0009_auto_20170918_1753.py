# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 12:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_dob2', '0008_mt_game_f_p1_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='mt_game',
            name='f_p2_start_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='mt_game',
            name='f_p3_start_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]