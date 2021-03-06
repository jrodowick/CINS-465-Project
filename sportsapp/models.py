# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

EVENT_CHOICES = (
    ('Soccer', "Soccer"),
    ('Football', "Football"),
    ('Baseball', "Baseball"),
    ('Wiffleball', "Wiffleball"),
    ('Ultimate Frisbee', "Ultimate Frisbee"),
    ('Basketball', "Basketball"),
    ('Disc Golf', "Disc Golf"),
)
class event(models.Model):
    event=models.CharField(choices=EVENT_CHOICES,max_length=40)
    create_time=models.DateTimeField(auto_now=True)
    location=models.CharField(max_length=140)
    date=models.DateField(max_length=280)

    def __str__(self):
        return self.sport

class team(models.Model):
    name=models.CharField(max_length=280)
    captain=models.CharField(max_length=40)

    def __str__(self):
        return self.name


# class Chat(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User)
#     message = models.CharField(max_length=200)
#
#     def __unicode__(self):
#         return self.message

# Create your models here.
