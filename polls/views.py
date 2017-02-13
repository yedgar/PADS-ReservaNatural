import json

from django.contrib.auth import authenticate, login, logout
from django.core import serializers

from django.http.response import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from polls.models import Usuario, Pais, Ciudad, Especie, Categoria


@csrf_exempt
def add_user_view(request):
    mensaje = ""
    if request.method == 'POST':
        password = request.POST['password']
        password2 = request.POST['password2']
        usuarios = Usuario.objects.filter(username=request.POST['username'])
        usuarios2 = Usuario.objects.filter(email=request.POST['email'])
        usuario = Usuario(username=request.POST['username'],
                          first_name=request.POST['first_name'],
                          last_name=request.POST['last_name'],
                          password=password,
                          email=request.POST['email'],
                          interes=request.POST['intereses'],
                          imageFile=request.FILES['fotoFile'],
                          ciudad_id=request.POST['ciudades']
                          )
        if password == password2:
            if not usuarios.exists() and not usuarios2.exists():
                usuario.set_password(password)
                usuario.save()
                mensaje = "ok"
            else:
                mensaje = "El usuario ya existe"
        else:
            mensaje = "Las contrasenas no coinciden"

    return JsonResponse({"mensaje": mensaje})

@csrf_exempt
def login_view(request):
    mensaje = ''
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            mensaje = "ok"
        else:
            mensaje = 'Nombre de usuario o clave no valido'
    return JsonResponse({"mensaje": mensaje})

@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"mensaje": "ok"})

@csrf_exempt
def islogged_view(request):
    if request.user.is_authenticated():
        mensaje = 'ok'
    else:
        mensaje = 'no'

    return JsonResponse({"mensaje": mensaje})

@csrf_exempt
def consultar_paises(request):
    qs = Pais.objects.all()
    qs_json = serializers.serialize('json', qs)
    return JsonResponse(qs_json, safe=False)

@csrf_exempt
def consultar_ciudades(request):
    qs = Ciudad.objects.filter(pais = request.GET['id'])
    qs_json = serializers.serialize('json', qs)
    return JsonResponse(qs_json, safe=False)

@csrf_exempt
def consultar_ciudad_user(request):
    user = request.user
    ciudad = user.ciudad.nombre
    return JsonResponse({'ciudad': ciudad})

@csrf_exempt
def consultar_pais_user(request):
    user = request.user
    pais = user.ciudad.pais.nombre
    return JsonResponse({'pais': pais})

@csrf_exempt
def obtener_especies(request):
    qs = Especie.objects.all()
    for especie in qs:
        especie.categoria_id = Categoria.objects.filter(id = especie.categoria_id).first().nombre
    qs_json = serializers.serialize('json', qs)
    return JsonResponse(qs_json, safe=False)

def is_logged_view(request):
    if request.user.is_authenticated():
        mensaje = 'ok'
    else:
        mensaje = 'no'
    return JsonResponse({'mensaje':mensaje})

@csrf_exempt
def obtener_infoUsuario(request):
    return HttpResponse(serializers.serialize("json", [request.user]))

@csrf_exempt
def editarUsuario(request):
    mensaje = ""
    if request.method == 'POST':

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        interes = request.POST['intereses']
        imageFile = request.FILES.get('fotoFile')
        ciudad_id = request.POST['ciudades']

        user = request.user

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.interes = interes
        if (imageFile != None):
            user.imageFile = imageFile
        user.ciudad_id = ciudad_id
        user.save()
        mensaje = "ok"

    return JsonResponse({'mensaje':mensaje})

@csrf_exempt
def mod_password_view(request):
    mensaje = ''
    if request.method == 'POST':
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            requestUser = Usuario.objects.get(username=request.user.username)
            requestUser.set_password(password)
            requestUser.save()
            user = authenticate(username=request.user.username, password=password)
            if user is not None:
                login(request, user)
                mensaje = "ok"
            else:
                mensaje = "Fail :("
        else:
            mensaje = "Las contrasenas no coinciden"

    return JsonResponse({"mensaje": mensaje})


def ir_index(request):
    return render(request,"polls/index.html")

def agregar_usuario(request):
    return render(request, "polls/registro.html")

def ingresar(request):
    return render(request, "polls/login.html")

def perfil(request):
    return render(request, "polls/perfil.html")

def modificar_password(request):
    return render(request, "polls/password.html")