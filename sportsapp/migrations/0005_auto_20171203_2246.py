# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 22:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsapp', '0004_remove_event_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event',
            new_name='name',
        ),
    ]
