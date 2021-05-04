#-*- coding: utf-8 -*-
from django import forms
# from .models import Dreamreal
from . import models

class LoginForm(forms.Form):
    user = forms.CharField(max_length = 4)
    password = forms.CharField(widget = forms.PasswordInput())

    def clean_message(self):
        username = self.cleaned_data.get("username")
        dbuser = models.Dreamreal.objects.filter(name = username)
        
        if not dbuser:
            raise forms.ValidationError("User does not exist in our db!")
        return username