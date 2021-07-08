from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Genero , Juego 


# Register your models here.

class JuegoAdmin(admin.ModelAdmin):
    list_display = ['nombre','codigo','valor','anio','genero','stock','sinopsis']
    search_fields = ['nombre','codigo']
    list_filter = ['genero']
    list_per_page = 10

admin.site.register(Genero)
admin.site.register(Juego, JuegoAdmin)