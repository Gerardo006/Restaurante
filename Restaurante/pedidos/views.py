# views.py
# views.py
import csv

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PedidoForm
from .models import Pedido


def realizarpedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el pedido en la base de datos
    else:
        form = PedidoForm()

    return render(request, 'realizarpedido.html', {'form': form})

def gestionpedidos(request):
    # Si es un POST, manejamos edición o eliminación
    if request.method == "POST":
        if "eliminar" in request.POST:  # Eliminar un pedido
            pedido_id = request.POST.get("pedido_identificador")
            pedido = get_object_or_404(Pedido, identificador=pedido_id)
            pedido.delete()
            return redirect('gestionpedidos')

        elif "editar" in request.POST:  # Editar un pedido
            pedido_id = request.POST.get("pedido_identificador")
            pedido = get_object_or_404(Pedido, identificador=pedido_id)
            form = PedidoForm(request.POST, instance=pedido)
            if form.is_valid():
                form.save()
                return redirect('gestionpedidos')

    elif request.method == "GET" and "informe_csv" in request.GET:  # Generar informe CSV
        pedidos = Pedido.objects.all()  # Obtener todos los pedidos
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="informe_pedidos.csv"'
        writer = csv.writer(response)
        writer.writerow(
            ['identificador', 'Nombre Cliente', 'Nombre Producto', 'Fecha',])  # Actualizar encabezados

        for pedido in pedidos:
            # Incluir el producto en lugar del estado
            writer.writerow(
                [pedido.identificador, pedido.nombre_cliente, pedido.producto.nombre, pedido.creado_en, pedido.total])

        return response

    # Obtener lista de pedidos
    pedidos = Pedido.objects.select_related('producto').all()  # Optimización con select_related si se usa FK o relación

    # Si se seleccionó un pedido para editar, cargarlo en el formulario
    pedido_a_editar = None
    form = None
    if request.GET.get("editar"):
        pedido_identificador = request.GET.get("editar")
        pedido_a_editar = get_object_or_404(Pedido, identificador=pedido_identificador)
        form = PedidoForm(instance=pedido_a_editar)

    return render(request, 'gestionpedidos.html', {
        'pedidos': pedidos,
        'form': form,
        'pedido_a_editar': pedido_a_editar,
    })

