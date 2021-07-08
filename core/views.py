from core.forms import JuegoForm
from django.shortcuts import redirect, render
from core.models import Juego
from django.contrib.auth.decorators import login_required, permission_required 

#rest_framework

from rest_framework import viewsets
from .serializers import JuegoSerializer

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def formulario(request):
    return render(request, 'core/formulario.html')

def galeria (request):
    return render(request, 'core/galeria.html' )

def listado_juegos (request):
    juegos = Juego.objects.all()

    data ={
        'juegos':juegos
    }

    return render(request , 'core/listado_juegos.html', data)

@permission_required('core.add_juego')
def nuevo_juego (request):
    data = {
        'form': JuegoForm()
    }
    if request.method == 'POST':
        formulario = JuegoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data ['mensaje'] = "Juego guardado correctamente"
        data['form'] = formulario
    return render(request, 'core/nuevo_juego.html', data )

@permission_required('core.change_juego')
def modificar_juego (request, id):
    juego = Juego.objects.get(id = id)
    data = {
        'form': JuegoForm(instance = juego)
    }

    if request.method == 'POST':
        formulario = JuegoForm(data = request.POST, instance = juego)
        if formulario.is_valid():
            formulario.save()
            data ['mensaje'] = "Juego modificado correctamente"
        data['form'] = formulario
            
    return render(request, 'core/modificar_juego.html', data )

@permission_required('core.delete_juego')
def eliminar_juego(request, id):
    juego = Juego.objects.get(id = id)
    juego.delete()
    return redirect(to = "listado_juegos")

class JuegoViewSet(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer