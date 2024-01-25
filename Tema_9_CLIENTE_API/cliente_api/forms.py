from django import forms
from django.forms import ModelForm
from .models import *
from datetime import date
import datetime
from .helpers import *

class BusquedaLibroForm(forms.Form):
    textoBusqueda = forms.CharField(required=True)

class BusquedaAvanzadaLibroForm(forms.Form):
    
    textoBusqueda = forms.CharField(required=False)
    
    IDIOMAS = [
        ("ES", "Español"),
        ("EN", "Inglés"),
        ("FR", "Francés"),
        ("IT", "Italiano"),
    ]
  
    idiomas = forms.MultipleChoiceField(choices=IDIOMAS,
                                required=False,
                                widget=forms.CheckboxSelectMultiple()
                               )
    
    fecha_desde = forms.DateField(label="Fecha Desde",
                                required=False,
                                widget= forms.SelectDateWidget(years=range(1990,2023))
                                )
    
    fecha_hasta = forms.DateField(label="Fecha Desde",
                                  required=False,
                                  widget= forms.SelectDateWidget(years=range(1990,2023))
                                  )
    
class LibroForm(forms.Form):
    nombre = forms.CharField(label="Nombre del Libro",
                             required=True, 
                             max_length=200,
                             help_text="200 caracteres como máximo")
    
    descripcion = forms.CharField(label="Descripcion",
                                  required=False,
                                  widget=forms.Textarea())
    
    fecha_publicacion = forms.DateField(label="Fecha Publicación",
                                        initial=datetime.date.today,
                                        widget= forms.SelectDateWidget()
                                        )
    
    IDIOMAS = [
        ("ES", "Español"),
        ("EN", "Inglés"),
        ("FR", "Francés"),
        ("IT", "Italiano"),
    ]
    idioma = forms.ChoiceField(choices=IDIOMAS,
                               initial="ES")
    
    bibliotecasDisponibles = obtener_bibliotecas_select()
    biblioteca = forms.ChoiceField(
            choices=bibliotecasDisponibles,
            widget=forms.Select,
            required=True,
    )
    
    autoresDisponibles = obtener_autores_select()
    autores = forms.MultipleChoiceField(
        choices= autoresDisponibles,
        required=True,
        help_text="Mantén pulsada la tecla control para seleccionar varios elementos"
    )
    