from django.urls import path

from  .api_views import *

urlpatterns = [
    path('libros',libro_list),
    path('libros/busqueda_simple',libro_buscar),
    path('libros/busqueda_avanzada',libro_buscar_avanzado),
    path('clientes',cliente_list)
]