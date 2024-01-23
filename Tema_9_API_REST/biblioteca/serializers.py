from rest_framework import serializers
from .models import *
                
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username','first_name']


class BibliotecarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibliotecario
        fields = '__all__'
    
class BibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = '__all__'
    
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
    
    
class LibroSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Libro
        
class LibroSerializerMejorado(serializers.ModelSerializer):
   
    #Para relaciones ManyToOne o OneToOne
    biblioteca = BibliotecaSerializer()
    
    #Para las relaciones ManyToMany
    autores = AutorSerializer(read_only=True, many=True)
    
    #Para formatear Fechas
    fecha_publicacion = serializers.DateField(format=('%d-%m-%Y'))
    
    #Para obtener el valor de un Choice
    idioma = serializers.CharField(source='get_idioma_display')
    
    class Meta:
        fields = ('nombre',
                  'idioma',
                  'descripcion',
                  'fecha_publicacion',
                  'biblioteca',
                  'autores')
        model = Libro


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    libros = PrestamoSerializer(read_only=True,source="prestamo_set",many=True)
    
    class Meta:
        model = Cliente
        fields = '__all__'


class DatosClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosCliente
        fields = '__all__'
