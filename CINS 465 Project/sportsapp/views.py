# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    form = SportsEvent()
    games = event.objects.all()
    to_return = []
    for game in games:
        data = {}
        data["event"]=game.event
        data["create_time"]=game.create_time
        to_return+=[data]
    context = {"games":games, "form":form}
    return render(request, "default.html", context)

def register(request):
    if request.method == 'POST':
        form = registration_form(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/")
    else:
        form = registration_form()
    context = {"form":form}
    return render(request,"register.html",context)

def sport_event(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            form = SportsEvent(request.POST,request.FILES)
            if form.is_valid():
                modentry = event(
                    event=form.cleaned_data['event'],
                )
                modentry.save()
                return redirect("/")
        else:
            form=SportsEvent()
    else:
        form = SportsEvent()
    context = {"form":form}
    return render(request,"event.html",context)

def team(request):
    if request.method=='POST':
        form = SportsEvent(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/")
    else:
        form = SportsEvent()
    context = {"form":form}
    return render(request,"team.html",context)
