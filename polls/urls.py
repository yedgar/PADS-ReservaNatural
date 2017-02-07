from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^add/$', views.add_image, name='addImage'),
    url(r'^addUser/$', views.add_user_view, name='addUser'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^consultarPaises/$', views.consultar_paises, name='consultarPaises'),
    url(r'^consultarCiudades/$', views.consultar_ciudades, name='consultarCiudades'),

    #url(r'^images/$', views.index, name='index'),
    url(r'^$', views.ir_index, name=''),
    url(r'^isLogged/$', views.islogged_view, name='isLogged'),
    url(r'^agregarImagen/$', views.agregar_imagen, name='agregarImagen'),
    url(r'^agregarUsuario/$', views.agregar_usuario, name='agregarUsuario'),
    url(r'^ingresar/$', views.ingresar, name='ingresar'),
]