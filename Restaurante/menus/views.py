

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from menus.models import Categoria
from .models import Menu, Producto
from .forms import MenuForm, ProductoForm, CategoriaForm


def menus(request):
    """
    Vista unificada para listar menús, categorías y productos y poder crear registros.
    """
    if not (request.user.is_staff or request.user.is_superuser):
        return render(request, '403.html', status=403)

    # Listar todos los registros
    menus = Menu.objects.all()
    categories = Categoria.objects.all()
    products = Producto.objects.all()

    # Inicializar los formularios vacíos
    menu_form = MenuForm()
    category_form = CategoriaForm()
    product_form = ProductoForm()

    # Procesar el formulario según la acción
    if request.method == 'POST':
        if 'create_menu' in request.POST:  # Crear un menú
            menu_form = MenuForm(request.POST)
            if menu_form.is_valid():
                menu_form.save()
                return redirect('menus')

        elif 'create_categoria' in request.POST:  # Crear una categoría
            category_form = CategoriaForm(request.POST)
            if category_form.is_valid():
                category_form.save()
                return redirect('menus')

        elif 'create_producto' in request.POST:  # Crear un producto
            product_form = ProductoForm(request.POST)
            if product_form.is_valid():
                product_form.save()
                return redirect('menus')

    return render(request, 'menus.html', {
        'menus': menus,
        'categorias': categories,
        'productos': products,
        'menu_form': menu_form,
        'categoria_form': category_form,
        'producto_form': product_form,
    })


def menuvista(request):
    """
    Vista para mostrar menús con sus categorías y productos en estructura jerárquica.
    """
    is_admin = request.user.is_staff or request.user.is_superuser

    # Obtenemos todos los menús activos
    menus_activos = Menu.objects.filter(estado=True)

    # Crear la estructura jerárquica
    menu_estructura = []
    for menu in menus_activos:
        categorias = Categoria.objects.filter(menu=menu)  # Categorías asociadas a este menú
        categorias_estructura = []

        for categoria in categorias:
            productos = Producto.objects.filter(categoria=categoria, disponibilidad=True).values(
                'id', 'nombre', 'precio', 'descripcion'
            )
            categorias_estructura.append({
                'id': categoria.id,
                'nombre': categoria.nombre,
                'productos': list(productos),
            })

        menu_estructura.append({
            'id': menu.id,
            'nombre': menu.nombre,
            'categorias': categorias_estructura,
        })

    # Retornar como JSON para solicitudes AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'menus': menu_estructura})

    # Renderizar la estructura en una plantilla
    return render(request, 'menuvista.html', {
        'menuestructura': menu_estructura,
        'is_admin': is_admin,
    })


def gestionarmenus(request):
    """
    Vista unificada para gestionar menús, categorías y productos (crear, actualizar, eliminar).
    """
    if not request.user.is_staff:
        return render(request, '403.html', status=403)

    # Recuperar parámetros para determinar acción (opcional)
    action = request.GET.get('action')  # acciones: create, update, delete
    type = request.GET.get('type')  # modelo: menu, categoria, producto
    object_id = request.GET.get('id')  # ID del objeto

    # Diccionario para manejar dinámicamente los modelos y formularios
    modelos = {
        'menu': (Menu, MenuForm),
        'categoria': (Categoria, CategoriaForm),
        'producto': (Producto, ProductoForm),
    }

    # Inicializar variables
    form = None
    objeto = None

    # Validar si el tipo corresponde a un modelo registrado
    if type in modelos:
        model, form_class = modelos[type]

        # Crear registro
        if action == 'create' and request.method == 'POST':
            form = form_class(request.POST)
            if form.is_valid():
                form.save()
                return redirect('gestionarmenus')

        elif action == 'update' and object_id:  # Actualizar un registro
            objeto = get_object_or_404(model, id=object_id)
            if request.method == 'POST':
                form = form_class(request.POST, instance=objeto)
                if form.is_valid():
                    form.save()
                    return redirect('gestionarmenus')
            else:
                form = form_class(instance=objeto)

        elif action == 'delete' and object_id:  # Eliminar un registro
            objeto = get_object_or_404(model, id=object_id)
            objeto.delete()
            return redirect('gestionarmenus')

    # Listar todos los registros
    menus = Menu.objects.all()
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()

    return render(request, 'gestionarmenus.html', {
        'menus': menus,
        'categorias': categorias,
        'productos': productos,
        'form': form,
        'objeto': objeto,
        'action': action,
        'type': type,
    })

