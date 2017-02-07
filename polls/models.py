from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    interes = models.CharField(max_length=1000)
    imageFile = models.ImageField(upload_to='images', null=True)