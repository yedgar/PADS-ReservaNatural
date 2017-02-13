from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^addUser/$', views.add_user_view, name='addUser'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^consultarPaises/$', views.consultar_paises, name='consultarPaises'),
    url(r'^consultarCiudades/$', views.consultar_ciudades, name='consultarCiudades'),
    url(r'^obtenerEspecies/$', views.obtener_especies, name='obtenerEspecies'),

    url(r'^$', views.ir_index, name=''),
    url(r'^isLogged/$', views.islogged_view, name='isLogged'),
    url(r'^agregarUsuario/$', views.agregar_usuario, name='agregarUsuario'),

    url(r'^verDetalle/$', views.obtener_especie, name='verDetalle'),
    url(r'^consultarEspecie/$', views.consultar_especie, name='consultarEspecie'),

    url(r'^ingresar/$', views.ingresar, name='ingresar'),
]