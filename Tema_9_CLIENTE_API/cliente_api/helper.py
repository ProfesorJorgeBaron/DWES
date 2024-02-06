
import requests
import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

class helper:

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
    
    def obtener_libro(id):
         # obtenemos todos los libros
        headers = {'Authorization': 'Bearer '+env("TOKEN_ACCESO")} 
        response = requests.get('http://127.0.0.1:8000/api/v1/libro/'+str(id),headers=headers)
        libro = response.json()
        return libro
    
    def obtener_token_session(usuario,password):
        token_url = 'http://127.0.0.1:8000/oauth2/token/'
        data = {
            'grant_type': 'password',
            'username': usuario,
            'password': password,
            'client_id': 'biblioteca',
            'client_secret': 'biblioteca',
        }

        response = requests.post(token_url, data=data)
        respuesta = response.json()
        if response.status_code == 200:
            return respuesta.get('access_token')
        else:
            raise Exception(respuesta.get("error_description"))