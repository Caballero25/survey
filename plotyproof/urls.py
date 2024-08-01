from django.urls import path
from .views import ingresar_coordenadas
from .views2 import trajectory_chart, trajectory_chart2D

urlpatterns = [
    #path('ingresar-coordenadas/', ingresar_coordenadas, name='ingresar_coordenadas'),
    path('', trajectory_chart, name='trajectory_chart'),
    path('2D', trajectory_chart2D, name='trajectory_chart2D')
]