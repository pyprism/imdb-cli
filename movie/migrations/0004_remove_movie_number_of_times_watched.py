# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 11:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20161115_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='number_of_times_watched',
        ),
    ]
