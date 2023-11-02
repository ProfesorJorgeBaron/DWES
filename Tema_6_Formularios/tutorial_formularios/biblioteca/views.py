from django.shortcuts import render,redirect
from django.db.models import Q,Prefetch
from django.forms import modelform_factory
from .models import *
from .forms import * 

# Create your views here.
def index(request):
    return render(request, 'index.html') 
    
def libro_create(request):
    
    # Si la petición es GET se creará el formulario Vacío
    # Si la petición es POST se creará el formulario con Datos.
    datosFormulario = None
    if request.method == "POST":
        datosFormulario = request.POST
    
    #formulario = LibroForm(datosFormulario)
    formulario = LibroModelForm(datosFormulario)
    """formularioFactory = modelform_factory(Libro, 
                                            fields='__all__',
                                            widgets = {
                                                "fecha_publicacion":forms.SelectDateWidget()
                                            })
    formulario = formularioFactory(datosFormulario)"""
    
    if (request.method == "POST"):
        # Llamamos la función que creará el libro
        #libro_creado = crear_libro_generico(formulario)
        libro_creado = crear_libro_modelo(formulario)
        if(libro_creado):
             return redirect("lista_libros")
        
    return render(request, 'libro/create.html',{"formulario":formulario})


def crear_libro_generico(formulario):
    libro_creado = False
    # Comprueba si el formulario es válido
    if formulario.is_valid():
        
        # Obtiene los datos del formulario validados correctamente. 
        libro = Libro.objects.create(
                nombre = formulario.cleaned_data.get('nombre'),
                idioma = formulario.cleaned_data.get('idioma'),
                descripcion = formulario.cleaned_data.get('descripcion'),
                fecha_publicacion = formulario.cleaned_data.get('fecha_publicacion'),
                biblioteca = formulario.cleaned_data.get('biblioteca'),
        )
        
        #Añade los autores que son relaciones ManyToMany
        libro.autores.set(formulario.cleaned_data.get('autores'))
        try:
            # Guarda el libro en la base de datos
            libro.save()
            libro_creado = True
        except:
            pass
    return libro_creado

def crear_libro_modelo(formulario):
    libro_creado = False
    # Comprueba si el formulario es válido
    if formulario.is_valid():
        try:
            # Guarda el libro en la base de datos
            formulario.save()
            libro_creado = True
        except:
            pass
    return libro_creado
    
    
def listar_libros(request):
    libros = Libro.objects.select_related("biblioteca").prefetch_related("autores")
    libros = libros.all()
    return render(request, 'libro/lista.html',{"libros_mostrar":libros})

#Páginas de Error
def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)