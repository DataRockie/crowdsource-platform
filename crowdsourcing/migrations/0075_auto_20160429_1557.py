# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-29 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0074_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationrecipient',
            name='status',
            field=models.SmallIntegerField(choices=[(1, b'Open'), (2, b'Minimized'), (3, b'Closed'), (4, b'Muted')], default=1),
        ),
        migrations.AlterField(
            model_name='taskworker',
            name='task_status',
            field=models.IntegerField(choices=[(1, b'In Progress'), (2, b'Submitted'), (3, b'Accepted'), (4, b'Rejected'), (5, b'Returned'), (6, b'Skipped'), (7, b'Expired')], default=1),
        ),
    ]
