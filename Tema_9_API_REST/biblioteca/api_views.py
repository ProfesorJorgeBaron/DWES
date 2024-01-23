from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .forms import *


@api_view(['GET'])
def libro_list(request):
    if(request.user.has_perm("biblioteca.view_libro")):
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)
        #serializer = LibroSerializerMejorado(libros, many=True)
        return Response(serializer.data)
    else:
        return Response({"Sin permisos"}, status=status.HTTP_401_UNAUTHORIZED)
    
'''   
    elif request.method == 'POST':
        
        datosFormulario = request.POST    
        formulario = LibroModelForm(datosFormulario)
        if formulario.is_valid():
            try:
                # Guarda el libro en la base de datos
                formulario.save()
                serializer = LibroSerializer(data=request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as error:
                Response(error, status=status.HTTP_400_BAD_REQUEST)

        return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)
'''