import csv

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from pyexpat.errors import messages
from django.contrib import messages
from .models import Categoria, Insumo, InventarioPrincipal, MovimientoInventario, ReporteConsumo
from .forms import CategoriaForm, InsumoForm, MovimientoInventarioForm

def inventario(request):
    """
    Vista consolidada para gestionar y visualizar categorías, insumos, inventario principal,
    movimientos de inventario y reportes de consumo en un formato similar al Django Admin.
    """
    # Listar todas las entidades
    categorias = Categoria.objects.all()
    insumos = Insumo.objects.all()
    inventario_principal = InventarioPrincipal.objects.all()
    movimientos = MovimientoInventario.objects.all()
    reportes_consumos = ReporteConsumo.objects.all()

    # Formularios vacíos para creación de instancias
    categoria_form = CategoriaForm()
    insumo_form = InsumoForm()
    movimiento_form = MovimientoInventarioForm()

    # Procesar operaciones POST (Crear/Actualizar/Eliminar)
    if request.method == 'POST':
        # Manejo de Categorías
        if 'crear_categoria' in request.POST:
            categoria_form = CategoriaForm(request.POST)
            if categoria_form.is_valid():
                categoria_form.save()
                return redirect('inventario')  # Cambia 'reporte_inventario' si el nombre de URL es diferente

        elif 'eliminar_categoria' in request.POST:
            categoria_id = request.POST.get('categoria_id')
            categoria = get_object_or_404(Categoria, id=categoria_id)
            categoria.delete()
            return redirect('inventario')

        # Manejo de Insumos
        elif 'crear_insumo' in request.POST:
            insumo_form = InsumoForm(request.POST)
            if insumo_form.is_valid():
                insumo_form.save()
                return redirect('reporte_inventario')

        elif 'eliminar_insumo' in request.POST:
            insumo_id = request.POST.get('insumo_id')
            insumo = get_object_or_404(Insumo, id=insumo_id)
            insumo.delete()
            return redirect('inventario')

        # Manejo de Movimientos de Inventarios
        elif 'crear_movimiento' in request.POST:
            movimiento_form = MovimientoInventarioForm(request.POST)
            if movimiento_form.is_valid():
                movimiento_form.save()
                return redirect('reporte_inventario')

        elif 'eliminar_movimiento' in request.POST:
            movimiento_id = request.POST.get('movimiento_id')
            movimiento = get_object_or_404(MovimientoInventario, id=movimiento_id)
            movimiento.delete()
            return redirect('inventario')

    # Renderizar la plantilla con los datos y formularios
    return render(request, 'inventario.html', {
        'categorias': categorias,
        'insumos': insumos,
        'inventario_principal': inventario_principal,
        'movimientos': movimientos,
        'reportes_consumos': reportes_consumos,
        'categoria_form': categoria_form,
        'insumo_form': insumo_form,
        'movimiento_form': movimiento_form,
    })

def inventariovista(request):
    """
    Vista para visualizar el inventario agrupado por categorías con sus insumos y disminuir el stock.
    """
    categorias_con_insumos = Categoria.objects.prefetch_related('insumo_set').all()

    # Manejar formulario de reducción de stock
    if request.method == 'POST':
        insumo_id = request.POST.get('insumo_id')
        cantidad_usar = request.POST.get('cantidad_usar')

        # Validar datos
        if insumo_id and cantidad_usar:
            try:
                cantidad_usar = int(cantidad_usar)
                insumo = get_object_or_404(Insumo, id=insumo_id)

                if cantidad_usar > 0 and cantidad_usar <= insumo.cantidad_disponible:
                    # Reducir stock del insumo
                    insumo.cantidad_disponible -= cantidad_usar
                    insumo.save()
                    messages.success(request, f'Se redujo el stock del insumo "{insumo.nombre}" en {cantidad_usar}.')
                else:
                    messages.error(request, f'La cantidad ingresada es inválida o excede el stock actual.')
            except ValueError:
                messages.error(request, f'Por favor, introduce un valor numérico válido.')
        else:
            messages.error(request, f'Los datos enviados son inválidos.')

        return redirect('vista_inventario')  # Redirigir a la misma página para evitar reenvío del formulario

    return render(request, 'inventariovista.html', {
        'categorias_con_insumos': categorias_con_insumos,
    })

def generar_reporte_consumos():
    """
    Genera un reporte de consumo en formato CSV.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporte_consumos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Insumo', 'Cantidad Consumida', 'Fecha de Consumo'])

    consumos = ReporteConsumo.objects.all()
    for consumo in consumos:
        writer.writerow([consumo.insumo.nombre, consumo.cantidad_consumida, consumo.fecha_consumo])

    return response


def generar_reporte_inventario():
    """
    Genera un reporte del inventario general en formato CSV.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporte_inventario.csv"'

    writer = csv.writer(response)
    writer.writerow(['Categoría', 'Insumo', 'Stock'])

    categorias = Categoria.objects.prefetch_related('insumo_set')
    for categoria in categorias:
        for insumo in categoria.insumo_set.all():
            writer.writerow([categoria.nombre, insumo.nombre, insumo.cantidad_disponible])

    return response