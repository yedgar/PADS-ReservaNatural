from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.
from django.forms.models import ModelForm


# class CustomUser(AbstractUser):
#    interes= models.CharField(max_length=1000)

class UserForm(ModelForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe email')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        password2 = self.data['password2']
        if password != password2:
            raise forms.ValidationError('Las claves no coinciden')
        return password2
