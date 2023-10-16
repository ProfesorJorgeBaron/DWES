from django.shortcuts import render
from django.db.models import Q
from .models import Libro,Cliente
from django.views.defaults import page_not_found

# Create your views here.
def index(request):
    return render(request, 'index.html') 

def listar_libros(request):
    libros = Libro.objects.all();
    return render(request, 'libro/lista.html',{"libros_mostrar":libros})

def dame_libro(request,id_libro):
    libro = Libro.objects.get(id=id_libro)
    return render(request, 'libro/libro.html',{"libro_mostrar":libro})

def dame_libros_fecha(request,anyo_libro,mes_libro):
    libros = Libro.objects.filter(fecha_publicacion__year=anyo_libro,fecha_publicacion__month=mes_libro)
    return render(request, 'libro/lista.html',{"libros_mostrar":libros})

def dame_libros_idioma(request,idioma):
    libros = Libro.objects.filter(Q(idioma=idioma) | Q(idioma="ES")).order_by("fecha_publicacion")
    return render(request, 'libro/lista.html',{"libros_mostrar":libros})

def dame_libros_biblioteca(request,id_biblioteca,texto_libro):
    libros = Libro.objects.filter(biblioteca=id_biblioteca).filter(descripcion__contains=texto_libro).order_by("-nombre")
    return render(request, 'libro/lista.html',{"libros_mostrar":libros})

def dame_ultimo_cliente_libro(request,libro):
    cliente = Cliente.objects.filter(prestamo__libro=libro).order_by("-prestamo__fecha_prestamo")[:1].get()
    return  render(request, 'cliente/cliente.html',{"cliente":cliente})


#Páginas de Error
def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)