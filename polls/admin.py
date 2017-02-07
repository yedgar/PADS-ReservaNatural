from django.contrib import admin

# from .models import Imagen
# Register your models here.
from polls.models import Categoria, Especie, Comentario, Usuario

admin.site.register(Categoria)
admin.site.register(Especie)
admin.site.register(Comentario)
admin.site.register(Usuario)