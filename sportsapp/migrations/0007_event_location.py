# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsapp', '0006_auto_20171203_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default=0, max_length=140),
            preserve_default=False,
        ),
    ]
