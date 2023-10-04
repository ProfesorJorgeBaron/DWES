from django.contrib import admin
from .models import Libro,Autor,Cliente,DatosCliente

# Register your models here.
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Cliente)
admin.site.register(DatosCliente)