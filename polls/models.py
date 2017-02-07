from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=100)

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True)

class Usuario(AbstractUser):
    interes = models.CharField(max_length=1000)
    imageFile = models.ImageField(upload_to='images', null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True)