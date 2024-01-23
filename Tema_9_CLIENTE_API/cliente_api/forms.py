from django import forms
from django.forms import ModelForm
from .models import *
from datetime import date
import datetime

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
    
    