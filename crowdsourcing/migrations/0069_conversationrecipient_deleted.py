# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-04 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0068_worker_scope'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversationrecipient',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]