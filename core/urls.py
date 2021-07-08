from django.db import router
from django.urls import path
from django.urls.conf import include 
from .views import eliminar_juego, index, modificar_juego 
from .views import formulario
from .views import galeria
from .views import listado_juegos
from .views import nuevo_juego

from .views import JuegoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('juegos', JuegoViewSet)

urlpatterns = [
    path('', index, name="index"),
    path('formulario/',formulario,name="formulario"),
    path('galeria/', galeria, name="galeria"),
    path('listado-juegos/', listado_juegos, name = "listado_juegos"),
    path('nuevo-juego/', nuevo_juego, name = "nuevo_juego"),
    path('modificar-juego/<id>/', modificar_juego, name = "modificar_juego"),
    path('eliminar-juego/<id>/', eliminar_juego , name="eliminar_juego"),
    path('api/', include(router.urls)),

]

