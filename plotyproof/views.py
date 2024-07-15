from django.shortcuts import render

# Create your views here.
import plotly.graph_objs as go
import plotly.io as pio
import numpy as np
from django import forms
from django.forms import formset_factory

class SegmentoForm(forms.Form):
    start_x = forms.FloatField(label='Inicio X')
    start_y = forms.FloatField(label='Inicio Y')
    start_z = forms.FloatField(label='Inicio Z')
    end_x = forms.FloatField(label='Fin X')
    end_y = forms.FloatField(label='Fin Y')
    end_z = forms.FloatField(label='Fin Z')
SegmentoFormSet = formset_factory(SegmentoForm, extra=1)


def ingresar_coordenadas(request):
    if request.method == 'POST':
        formset = SegmentoFormSet(request.POST)
        if formset.is_valid():
            segmentos = []
            for form in formset:
                if form.cleaned_data:
                    segmento = {
                        'start': [form.cleaned_data['start_x'], form.cleaned_data['start_y'], form.cleaned_data['start_z']],
                        'end': [form.cleaned_data['end_x'], form.cleaned_data['end_y'], form.cleaned_data['end_z']]
                    }
                    segmentos.append(segmento)
            grafico_html = generar_tuberias(segmentos)
            return render(request, 'pipeline_3d.html', {'grafico': grafico_html})
    else:
        # Valores iniciales predeterminados
        initial_data = [
            {'start_x': 0, 'start_y': 0, 'start_z': 0, 'end_x': 5, 'end_y': 5, 'end_z': 5},
            {'start_x': 5, 'start_y': 5, 'start_z': 5, 'end_x': 10, 'end_y': 0, 'end_z': 5},
            {'start_x': 10, 'start_y': 0, 'start_z': 5, 'end_x': 15, 'end_y': 5, 'end_z': 0},
            {'start_x': 15, 'start_y': 5, 'start_z': 0, 'end_x': 20, 'end_y': 10, 'end_z': 5},
            {'start_x': 20, 'start_y': 10, 'start_z': 5, 'end_x': 25, 'end_y': 5, 'end_z': 10},
            {'start_x': 25, 'start_y': 5, 'start_z': 10, 'end_x': 30, 'end_y': 0, 'end_z': 5},
            {'start_x': 10, 'start_y': 0, 'start_z': 5, 'end_x': 10, 'end_y': -5, 'end_z': 0},
            {'start_x': 10, 'start_y': -5, 'start_z': 0, 'end_x': 15, 'end_y': -10, 'end_z': -5},
            {'start_x': 20, 'start_y': 10, 'start_z': 5, 'end_x': 25, 'end_y': 15, 'end_z': 10},
            {'start_x': 25, 'start_y': 15, 'start_z': 10, 'end_x': 30, 'end_y': 20, 'end_z': 15},
            {'start_x': 30, 'start_y': 0, 'start_z': 5, 'end_x': 35, 'end_y': -5, 'end_z': 10},
            {'start_x': 35, 'start_y': -5, 'start_z': 10, 'end_x': 40, 'end_y': -10, 'end_z': 15}
        ]
        formset = SegmentoFormSet(initial=initial_data)
        
    
    return render(request, 'ingresar_coordenadas.html', {'formset': formset})

def generar_tuberias(segmentos):
    data = []

    for segmento in segmentos:
        x = [segmento['start'][0], segmento['end'][0]]
        y = [segmento['start'][1], segmento['end'][1]]
        z = [segmento['start'][2], segmento['end'][2]]
        
        # Agregar segmento de tubería
        trace = go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color='blue', width=10))
        data.append(trace)

        # Agregar los puntos de inicio y fin para cada segmento
        trace_start = go.Scatter3d(x=[segmento['start'][0]], y=[segmento['start'][1]], z=[segmento['start'][2]], 
                                   mode='markers', marker=dict(color='red', size=5))
        trace_end = go.Scatter3d(x=[segmento['end'][0]], y=[segmento['end'][1]], z=[segmento['end'][2]], 
                                 mode='markers', marker=dict(color='green', size=5))
        data.append(trace_start)
        data.append(trace_end)

    # Crear el layout
    layout = go.Layout(title='Simulación de Tuberías Petroleras', scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ))

    # Crear la figura
    fig = go.Figure(data=data, layout=layout)

    # Obtener el HTML del gráfico
    grafico_html = pio.to_html(fig, full_html=False)

    return grafico_html



