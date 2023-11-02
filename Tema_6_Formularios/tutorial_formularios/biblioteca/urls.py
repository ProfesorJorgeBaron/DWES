from django.urls import path,re_path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    
    path('libro/create/',views.libro_create,name='libro_create'),
    
    path('libros/listar',views.listar_libros,name='lista_libros'),
]