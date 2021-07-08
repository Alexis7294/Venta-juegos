from rest_framework import fields, serializers
from .models import Juego

class JuegoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Juego
        fields = ['nombre','codigo','valor','anio','genero','stock','sinopsis']