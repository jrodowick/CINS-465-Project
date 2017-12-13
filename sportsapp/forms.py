from django import forms
from django.core.validators import validate_unicode_slug

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Form

import datetime

from .models import *
from .models import EVENT_CHOICES

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={
        'name':'username'
        })
    )
    password=forms.CharField(
        label="Password",
        max_length=32,
        widget=forms.PasswordInput()
    )

class registration_form(UserCreationForm):
    email=forms.EmailField(
        label="Email",
        required=True
    )

class Meta:
    model=User
    fields=("username","email","password1","password2")

    def save(self,commit=True):
        user=super(registration_form,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class SportsEvent(forms.Form):
    event=forms.ChoiceField(
        label="Sports Event",
        choices=EVENT_CHOICES,
    )
    location=forms.CharField(
        label="Location",
    )
    date=forms.DateField(
        widget = SelectDateWidget
    )

    def save(self, request, commit=True):
        game = event()
        game.event=self.cleaned_data['event']
        game.location=self.cleaned_data['location']
        game.date=self.cleaned_data['date']
        if commit:
            game.save()
        return game

class BuildTeam(forms.Form):
    name=forms.CharField(
        label="Team Name",
        max_length=280
    )
    captain=forms.CharField(
        label="Team Captain",
        max_length="40"
    )
    

    def save(self, request, commit=True):
        a_team = team()
        a_team.name=self.cleaned_data['name']
        a_team.captain=self.cleaned_data['captain']
        if commit:
            a_team.save()
        return a_team
