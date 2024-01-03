from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    
    path('libros/listar',views.libros_lista,name='libro_lista'),
    
]