class cliente_api:
    codigo = 0
    datos = None
    
    def realizar_peticion_api(url,metodo,datos=None):
    
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

        
