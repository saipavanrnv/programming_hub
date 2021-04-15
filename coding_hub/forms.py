"""
forms.py
author: Mukesh
Date: 11/22/2020
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class NewUserForm(UserCreationForm):
    """
    Used for register account
    """
    group = forms.ModelChoiceField(queryset=Group.objects.all().exclude(name = "Instructor"), required=True)
    class Meta: #pylint: disable=too-few-public-methods
        """
        For including fields for register
        """
        model = User
        fields = ("username", "email", "password1", "password2","group")
