from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields= '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = [
            'username',
            'password1',
            'password2'
        ]