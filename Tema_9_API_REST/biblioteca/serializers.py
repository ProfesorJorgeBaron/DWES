from rest_framework import serializers
from .models import *
from .forms import *
                
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
        fields = ('id',
                  'nombre',
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


class LibroSerializerCreate(serializers.ModelSerializer):
 
    class Meta:
        model = Libro
        fields = ['nombre','descripcion','fecha_publicacion',
                  'idioma','biblioteca','autores',
                  'fecha_actualizacion']
    
    def validate_nombre(self,nombre):
        libroNombre = Libro.objects.filter(nombre=nombre).first()
        if(not libroNombre is None
           ):
             if(not self.instance is None and libroNombre.id == self.instance.id):
                 pass
             else:
                raise serializers.ValidationError('Ya existe un libro con ese nombre')
            
        
        return nombre
    
    def validate_descripcion(self,descripcion):
        if len(descripcion) < 10:
             raise serializers.ValidationError('Al menos debes indicar 10 caracteres')
        return descripcion
    
    def validate_fecha_publicacion(self,fecha_publicacion):
        fechaHoy = date.today()
        if fechaHoy >= fecha_publicacion:
            raise serializers.ValidationError('La fecha de publicacion debe ser mayor a Hoy')
        return fecha_publicacion
    
    def validate_biblioteca(self,biblioteca): 
        if self.initial_data['idioma'] == "FR" and biblioteca == 1:
            raise serializers.ValidationError('No puede usar la Biblioteca de la Universidad de Sevilla y el idioma Fránces')
        return biblioteca
    
    def validate_idioma(self,idioma): 
        if idioma == "FR" and int(self.initial_data['biblioteca']) == 1:
            raise serializers.ValidationError('No puede usar la Biblioteca de la Universidad de Sevilla y el idioma Fránces')
        return idioma
    
    def validate_autores(self,autores):
        if len(autores) < 1:
            raise serializers.ValidationError('Debe seleccionar al menos un autor')
        return autores

class LibroSerializerActualizarNombre(serializers.ModelSerializer):
 
    class Meta:
        model = Libro
        fields = ['nombre']
    
    def validate_nombre(self,nombre):
        libroNombre = Libro.objects.filter(nombre=nombre).first()
        if(not libroNombre is None and libroNombre.id != self.instance.id):
            raise serializers.ValidationError('Ya existe un libro con ese nombre')
        return nombre