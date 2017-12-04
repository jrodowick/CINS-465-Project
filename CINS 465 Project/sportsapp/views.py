# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from itertools import chain

from .models import *
from .forms import *

# Create your views here.
def index(request):
    form = SportsEvent()
    games = event.objects.all()
    return render(request, "default.html", {'games':games})

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
                    location=form.cleaned_data['location'],
                    date=form.cleaned_data['date']
                )
                modentry.save()
                return redirect("/")
        else:
            form=SportsEvent()
    else:
        form = SportsEvent()
    games = event.objects.all()
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
