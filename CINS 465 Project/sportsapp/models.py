# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class new_event(models.Model):
    event=models.CharField(max_length=280)
    create_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event

# class Chat(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User)
#     message = models.CharField(max_length=200)
#
#     def __unicode__(self):
#         return self.message

# Create your models here.
