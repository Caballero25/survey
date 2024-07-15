from django.shortcuts import render
from django.http import JsonResponse
import plotly.graph_objects as go
from plotly.offline import plot

def trajectory_chart(request):
    demostrativo = True  # Cambia a False si no quieres los datos de demostración

    if request.method == 'POST':
        x = request.POST.getlist('x[]')
        y = request.POST.getlist('y[]')
        z = request.POST.getlist('z[]')

        x = [float(i) for i in x]
        y = [float(i) for i in y]
        z = [float(i) for i in z]

        # Crear la figura 3D
        fig_3d = go.Figure(data=[go.Scatter3d(
            x=x, y=y, z=z,
            mode='lines+markers',
            marker=dict(size=5),
            line=dict(color='blue', width=2)
        )])

        # Configurar el diseño del gráfico 3D
        fig_3d.update_layout(
            title='Gráfico 3D de la trayectoria del pozo',
            scene=dict(
                xaxis_title='N/S (ft)',
                yaxis_title='E/W (ft)',
                zaxis_title='TVD (ft)'
            )
        )

        # Generar los gráficos Plotly
        plot_div_3d = plot(fig_3d, output_type='div')
        return JsonResponse({'plot_div_3d': plot_div_3d})

    # En caso de GET request, renderiza la plantilla con un gráfico vacío
    fig_3d = go.Figure()
    plot_div_3d = plot(fig_3d, output_type='div')
    return render(request, 'trajectory_chart.html', context={'plot_div_3d': plot_div_3d, 'demostrativo': demostrativo})


"""
# Crear la figura 2D
    fig_2d = go.Figure()
    fig_2d.add_trace(go.Scatter(
        x=v_sec, y=md,
        mode='lines+markers',
        marker=dict(size=5),
        line=dict(color='red', width=2),
        name='MD vs V. sec.'
    ))

    # Configurar el diseño del gráfico 2D
    fig_2d.update_layout(
        title='Gráfico 2D de la trayectoria del pozo',
        xaxis_title='V. sec. (ft)',
        yaxis_title='MD (ft)'
    )
        plot_div_2d = plot(fig_2d, output_type='div')
        , 'plot_div_2d': plot_div_2d
"""