
import requests
import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'),True)
env = environ.Env()


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
    
    def obtener_categorias_select():
        # obtenemos todos los libros
        headers = {'Authorization': 'Bearer '+env("TOKEN_ACCESO")} 
        response = requests.get('http://127.0.0.1:8000/api/v1/categorias',headers=headers)
        categorias = response.json()
        lista_categorias = []
        for categoria in categorias:
            lista_categorias.append((categoria["id"],categoria["categoria"]))
        return lista_categorias
    
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
        
    def calsificar_texto(text):
        key = "543401d0-c982-11ee-8c3f-15f879bf0d6e9c43b3af-55a3-4803-8cf8-f424b47f9366"
        url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

        response = requests.get(url, params={ "data" : text })

        if response.ok:
            responseData = response.json()
            topMatch = responseData[0]
            return topMatch
        else:
            response.raise_for_status()
            
    
    def realizar_peticion_api(url,metodo,datos=None,formulario=None):
    
        codigo = 0
        try:
            if metodo == "PUT" or metodo == "PATCH" or metodo == "POST":
                headers = crear_cabecera_contenido()
            else:
                headers = crear_cabecera_token()
            
            if(datos is not None):
                datos=json.dumps(datos)
            
            response = requests.put(
                env("URL")+url,
                headers=headers,
                data=datos
            )
            codigo = response.status_code
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')
        except Exception as err:
            print(f'Ocurrió un error: {err}')
        return codigo
        
        
    def mis_errores(code,formulario,url_respuesta,datosrespuesta):
        if code == 400:
            # Error de que la solicitud no pudo ser interpretada o estaba mal formada.
            errores = response.json()
            for error in errores:
                formulario.add_error(error,errores[error])
                return render(request, url_respuesta,datosrespuesta)
        elif code == 401:
            # Error de credenciales de auntenticación inválidas.
            return mi_error_401(request) 
        elif response.status_code == 403:
            # Error de permisos de usuario.
            return mi_error_403(request)
        elif response.status_code == 404:
            # Error de recurso no encontrado.
            return mi_error_404(request)
        else:
            # Otros tipos de errores
            return mi_error_500(request)

        
