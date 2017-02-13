from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^addUser/$', views.add_user_view, name='addUser'),
    url(r'^modPassword/$', views.mod_password_view, name='modPassword'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^consultarPaises/$', views.consultar_paises, name='consultarPaises'),
    url(r'^consultarCiudades/$', views.consultar_ciudades, name='consultarCiudades'),
    url(r'^obtenerEspecies/$', views.obtener_especies, name='obtenerEspecies'),

    url(r'^$', views.ir_index, name=''),
    url(r'^isLogged/$', views.islogged_view, name='isLogged'),
    url(r'^agregarUsuario/$', views.agregar_usuario, name='agregarUsuario'),
    url(r'^ingresar/$', views.ingresar, name='ingresar'),
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^infoUsuario/$', views.obtener_infoUsuario, name='infoUsuario'),
    url(r'^consultarCiudadUser/$', views.consultar_ciudad_user, name='consultarCiudadUser'),
    url(r'^consultarPaisUser/$', views.consultar_pais_user, name='consultarPaisUser'),
    url(r'^editarUsuario/$', views.editarUsuario, name='editarUsuario'),
    url(r'^modificarPassword/$', views.modificar_password, name='modificarPassword'),
]