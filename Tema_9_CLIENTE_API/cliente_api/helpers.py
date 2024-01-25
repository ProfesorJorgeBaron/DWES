
import requests
import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


def obtener_bibliotecas_select():
     # obtenemos todos los libros
    headers = {'Authorization': 'Bearer '+env("TOKEN_ACCESO")} 
    response = requests.get('http://127.0.0.1:8000/api/v1/bibliotecas',headers=headers)
    bibliotecas = response.json()
    
    lista_bibliotecas = [("","Ninguna")]
    for biblioteca in bibliotecas:
        lista_bibliotecas.append((biblioteca["id"],biblioteca["nombre"]))
    return lista_bibliotecas

def obtener_autores_select():
     # obtenemos todos los libros
    headers = {'Authorization': 'Bearer '+env("TOKEN_ACCESO")} 
    response = requests.get('http://127.0.0.1:8000/api/v1/autores',headers=headers)
    autores = response.json()
    lista_autores = []
    for autor in autores:
        lista_autores.append((autor["id"],autor["nombre"]))
    return lista_autores