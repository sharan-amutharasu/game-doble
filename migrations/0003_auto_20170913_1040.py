# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-13 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_dob2', '0002_auto_20170913_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='mt_game',
            name='f_key',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='mt_game',
            name='f_set1',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='mt_game',
            name='f_set2',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='mt_game',
            name='f_set3',
            field=models.CharField(default='none', max_length=100),
        ),
    ]