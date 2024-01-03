from django.shortcuts import render

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

def libros_lista(request):
    # obtenemos todos los libros
    #headers = {'Authorization': 'Bearer VbIK1VNOGu9o7eZm58Z70RIuJrIv7H'} 
    headers = {'Authorization': 'Bearer '+env("TOKEN_ACCESO")} 
    response = requests.get('http://127.0.0.1:8000/api/v1/libros',headers=headers)
    print(response)
   # Transformamos la respuesta en json
    libros = response.json()
    #return render(request, 'libro/lista.html',{"libros_mostrar":libros})
    return render(request, 'libro/lista_mejorada.html',{"libros_mostrar":libros})