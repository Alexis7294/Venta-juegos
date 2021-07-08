from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.IntegerField()
    valor = models.IntegerField()
    anio = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=CASCADE)
    stock = models.IntegerField()
    sinopsis = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre
