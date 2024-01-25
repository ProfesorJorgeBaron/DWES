from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .forms import *
from django.db.models import Q,Prefetch

@api_view(['GET'])
def libro_list(request):
    if(request.user.has_perm("biblioteca.view_libro")):
        libros = Libro.objects.select_related("biblioteca").prefetch_related("autores").all()
        #serializer = LibroSerializer(libros, many=True)
        serializer = LibroSerializerMejorado(libros, many=True)
        return Response(serializer.data)
    else:
        return Response({"Sin permisos"}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
def cliente_list(request):
    clientes = Cliente.objects.all()
    serializer = ClienteSerializer(clientes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def libro_buscar(request):
    if(request.user.has_perm("biblioteca.view_libro")):
        formulario = BusquedaLibroForm(request.query_params)
        if(formulario.is_valid()):
            texto = formulario.data.get('textoBusqueda')
            libros = Libro.objects.select_related("biblioteca").prefetch_related("autores")
            libros = libros.filter(Q(nombre__contains=texto) | Q(descripcion__contains=texto)).all()
            serializer = LibroSerializerMejorado(libros, many=True)
            return Response(serializer.data)
        else:
            return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"Sin permisos"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def libro_buscar_avanzado(request):

    if(len(request.query_params) > 0):
        formulario = BusquedaAvanzadaLibroForm(request.query_params)
        if formulario.is_valid():
            texto = formulario.cleaned_data.get('textoBusqueda')
            QSlibros = Libro.objects.select_related("biblioteca").prefetch_related("autores")
            
            #obtenemos los filtros
            textoBusqueda = formulario.cleaned_data.get('textoBusqueda')
            idiomas = formulario.cleaned_data.get('idiomas')
            fechaDesde = formulario.cleaned_data.get('fecha_desde')
            fechaHasta = formulario.cleaned_data.get('fecha_hasta')
            
            #Por cada filtro comprobamos si tiene un valor y lo añadimos a la QuerySet
            if(textoBusqueda != ""):
                QSlibros = QSlibros.filter(Q(nombre__contains=texto) | Q(descripcion__contains=texto))
                
            #Si hay idiomas, iteramos por ellos, creamos la queryOR y le aplicamos el filtro
            if(len(idiomas) > 0):
                filtroOR = Q(idioma=idiomas[0])
                for idioma in idiomas[1:]:
                    mensaje_busqueda += " o "+idiomas[1]
                    filtroOR |= Q(idioma=idioma)
                QSlibros =  QSlibros.filter(filtroOR)
            
            #Comprobamos fechas
            #Obtenemos los libros con fecha publicacion mayor a la fecha desde
            if(not fechaDesde is None):
                QSlibros = QSlibros.filter(fecha_publicacion__gte=fechaDesde)
            
             #Obtenemos los libros con fecha publicacion menor a la fecha desde
            if(not fechaHasta is None):
                QSlibros = QSlibros.filter(fecha_publicacion__lte=fechaHasta)
            
            libros = QSlibros.all()
            serializer = LibroSerializerMejorado(libros, many=True)
            return Response(serializer.data)
        else:
            return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
def biblioteca_list(request):
    bibliotecas = Biblioteca.objects.all()
    serializer = BibliotecaSerializer(bibliotecas, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def autor_list(request):
    autores = Autor.objects.all()
    serializer = AutorSerializer(autores, many=True)
    return Response(serializer.data)
'''
@api_view(['POST'])
def libro_create(request):
    formulario = LibroModelForm(request.query_params)
    if formulario.is_valid():
        try:
            formulario.save()
            return Response("Libro CREADO")
        except Exception as error:
            print(error)
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)
'''

@api_view(['POST'])
def libro_create(request):
    serializers = LibroSerializerCreate(data=request.query_params)
    if serializers.is_valid():
        try:
            serializers.save()
            return Response("Libro CREADO")
        except Exception as error:
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    