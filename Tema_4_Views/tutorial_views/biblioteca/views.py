from django.shortcuts import render
from .models import Libro
# Create your views here.

# Create your views here.
def index(request):
    return render(request, 'index.html') 

def listar_libros(request):
    libros = Libro.objects.all();
    return render(request, 'libro/lista.html',{"libros_mostrar":libros}) 