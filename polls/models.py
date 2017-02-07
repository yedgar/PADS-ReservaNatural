from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Especie(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_cientifico = models.CharField(max_length=100)
    clasificacion_taxonomica = models.CharField(max_length=200)
    descripcion_corta = models.CharField(max_length=200)
    descripcion_larga = models.CharField(max_length=500)
    fotoFile = models.ImageField(upload_to='images', null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)

class Comentario(models.Model):
    descripcion = models.CharField(max_length=500)
    correo_electronico = models.CharField(max_length=100)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, null=True)

class Pais(models.Model):
    nombre = models.CharField(max_length=100)

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True)

class Usuario(AbstractUser):
    interes = models.CharField(max_length=1000)
    imageFile = models.ImageField(upload_to='images', null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True)