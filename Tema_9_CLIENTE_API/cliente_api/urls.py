from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    
    path('libros/listar',views.libros_lista,name='libro_lista'),
    path('libros/busqueda_simple',views.libro_busqueda_simple,name='libro_buscar_simple'),
    path('libros/busqueda_avanzada',views.libro_busqueda_avanzada,name='libro_buscar_avanzado'),
    
]