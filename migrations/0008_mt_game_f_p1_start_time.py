# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 12:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_dob2', '0007_auto_20170916_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='mt_game',
            name='f_p1_start_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
