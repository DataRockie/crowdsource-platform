# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-08 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0079_auto_20160508_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='time_spent',
            field=models.IntegerField(default=0),
        ),
    ]