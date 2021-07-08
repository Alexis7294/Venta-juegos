from django import forms
from django.forms import ModelForm, fields
from .models import Juego

class JuegoForm(ModelForm):

    class Meta:
        model = Juego
        fields = ['nombre','codigo','valor','anio','genero','stock', 'sinopsis']

        