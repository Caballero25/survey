from django.urls import path
from .views import ingresar_coordenadas
from .views2 import trajectory_chart

urlpatterns = [
    #path('ingresar-coordenadas/', ingresar_coordenadas, name='ingresar_coordenadas'),
    path('', trajectory_chart, name='trajectory_chart'),
]