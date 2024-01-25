from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
# Create your views here.
#Vistas API


import requests
import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Create your views here.
def index(request):
    return render(request, 'index.html')

def crear_cabecera():
    return {'Authorization': 'Bearer '+env("TOKEN_ACCESO")}

def libros_lista(request):
    # obtenemos todos los libros
    #headers = {'Authorization': 'Bearer SlNWDzValrcSZ2QGrI8Nx3lFwEKTou'} 
    headers = {'Authorization': 'Bearer '+env("TOKEN_ACCESO")} 
    response = requests.get('http://127.0.0.1:8000/api/v1/libros',headers=headers)
   # Transformamos la respuesta en json
    libros = response.json()
    #return render(request, 'libro/lista.html',{"libros_mostrar":libros})
    return render(request, 'libro/lista_mejorada.html',{"libros_mostrar":libros})


def libro_busqueda_simple(request):
    formulario = BusquedaLibroForm(request.GET)
    
    if formulario.is_valid():
        headers = crear_cabecera()
        response = requests.get(
            'http://127.0.0.1:8000/api/v1/libros/busqueda_simple',
            headers=headers,
            params=formulario.cleaned_data
        )
        libros = response.json()
        return render(request, 'libro/lista_mejorada.html',{"libros_mostrar":libros})
    if("HTTP_REFERER" in request.META):
        return redirect(request.META["HTTP_REFERER"])
    else:
        return redirect("index")
    
from requests.exceptions import HTTPError
def libro_busqueda_avanzada(request):
    if(len(request.GET) > 0):
        formulario = BusquedaAvanzadaLibroForm(request.GET)
        
        try:
            headers = crear_cabecera()
            response = requests.get(
                'http://127.0.0.1:8000/api/v1/libros/busqueda_avanzada',
                headers=headers,
                params=formulario.data
            )             
            if(response.status_code == requests.codes.ok):
                libros = response.json()
                return render(request, 'libro/lista_mejorada.html',
                              {"libros_mostrar":libros})
            else:
                print(response.status_code)
                response.raise_for_status()
        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')
            if(http_err == 400):
                errores = response.json()
                for error in errores:
                    formulario.add_error(error,errores[error])
                return render(request, 
                            'libro/busqueda_avanzada.html',
                            {"formulario":formulario,"errores":errores})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
    else:
        formulario = BusquedaAvanzadaLibroForm(None)
    return render(request, 'libro/busqueda_avanzada.html',{"formulario":formulario})

def libro_crear(request):
    
    if (request.method == "POST"):
        formulario = LibroForm(request.POST)
        headers = crear_cabecera()
        datos = formulario.data
        datos["fecha_publicacion"] = datetime.date(year=int(datos['fecha_publicacion_year']),
                                                    month=int(datos['fecha_publicacion_month']),
                                                    day=int(datos['fecha_publicacion_day']))
        
        response = requests.post(
            'http://127.0.0.1:8000/api/v1/libros/crear',
            headers=headers,
            params=formulario.data
        )
        if(response.status_code == requests.codes.ok):
            return redirect("libro_lista")
        else:
            errores = response.json()
            for error in errores:
                formulario.add_error(error,errores[error])
    else:
         formulario = LibroForm(None)
    return render(request, 'libro/create.html',{"formulario":formulario})

#Páginas de Error
def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

#Páginas de Error
def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)

