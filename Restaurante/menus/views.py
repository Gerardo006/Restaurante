

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from menus.models import Categoria, Menu, Producto
from .forms import MenuForm, ProductoForm, CategoriaForm
from .services import get_recipe_by_id, search_recipes


def menus(request):
    """
    Vista unificada para listar menús, categorías y productos y poder crear registros.
    """
    if not (request.user.is_staff or request.user.is_superuser):
        return render(request, '403.html', status=403)

    # Listar todos los registros
    menus = Menu.objects.all()
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()

    # Inicializar los formularios vacíos
    menu_form = MenuForm()
    categoria_form = CategoriaForm()
    producto_form = ProductoForm()

    # Procesar el formulario según la acción
    if request.method == 'POST':
        if 'create_menu' in request.POST:  # Crear un menú
            menu_form = MenuForm(request.POST)
            if menu_form.is_valid():
                menu_form.save()
                return redirect('menus')

        elif 'create_categoria' in request.POST:  # Crear una categoría
            categoria_form = CategoriaForm(request.POST)
            if categoria_form.is_valid():
                categoria_form.save()
                return redirect('menus')

        elif 'create_producto' in request.POST:  # Crear un producto
            producto_form = ProductoForm(request.POST)
            if producto_form.is_valid():
                producto_form.save()
                return redirect('menus')


    return render(request, 'menus.html', {
        'menu': menus,
        'categoria': categorias,
        'producto': productos,
        'menu_form': menu_form,
        'categoria_form': categoria_form,
        'producto_form': producto_form,
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
            productos = Producto.objects.filter(categoria=categoria).values(
                 'nombre', 'precio',
            )
            categorias_estructura.append({
                'nombre': categoria.nombre,
                'productos': list(productos),
            })

        menu_estructura.append({
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

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el producto en la base de datos
            return redirect('menuvista')  # Redirige a la lista de productos

    else:
        form = ProductoForm()

    return render(request, 'detalle_receta.html', {'form': form})

def buscar_recetas(request):
    """
    Vista principal para buscar recetas mediante un término.
    """
    query = request.GET.get('query', '')  # Recuperar el término desde el formulario
    recetas = []

    if query:  # Si el usuario ingresó una búsqueda
        try:
            recetas = search_recipes(query)  # Llama al servicio
        except Exception as e:
            print(f"Error al llamar a la API: {e}")
            recetas = []  # Vacía en caso de error

    return render(request, 'buscar_recetas.html', {'recetas': recetas, 'query': query})


def detalle_receta(request, receta_id):
    """
    Vista para mostrar los detalles de una receta específica.
    """
    receta = None

    try:
        receta = get_recipe_by_id(receta_id)  # Servicio para detalles
    except Exception as e:
        print(f"Error al obtener la receta: {e}")

    return render(request, 'detalle_receta.html', {'receta': receta})