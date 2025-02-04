from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from pyexpat.errors import messages

from .models import Mesa, Reserva
from .forms import MesaForm, ReservaForm


def home(request):
    if request.method == 'POST':  # Si es una solicitud de inicio de sesión
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('paneladmin')  # Cambia 'url_destino' por el nombre de tu URL o vista
        else:
            messages.error(request, 'Credenciales incorrectas. Por favor, inténtalo de nuevo.')

        # Renderiza el formulario de inicio de sesión
    return render(request, 'home.html')

def crearmesas(request):
    """Vista para crear mesas."""
    if request.method == "POST":
        mesa_form = MesaForm(request.POST)

        if mesa_form.is_valid():
            # Guardar la mesa
            mesa_form.save()
            return redirect('crearmesas')  # Cambia por la vista de éxito o redirección deseada
    else:
        mesa_form = MesaForm()

    context = {
        'mesa_form': mesa_form
    }
    return render(request, 'crearmesas.html', context)

def listarmesas(request):
    """Vista para listar todas las mesas junto con su ubicación y formulario de reserva."""
    mesas = Mesa.objects.all()  # Obtén todas las mesas de la base de datos

    # Si se envía una reserva
    if request.method == 'POST':
        form = ReservaForm(request.POST)  # Instanciar formulario con los datos enviados
        if form.is_valid():  # Validar el formulario
            # Obtener la mesa específica relacionada con la reserva
            mesa = get_object_or_404(Mesa, id=request.POST.get('mesa_id'))  # Buscar la mesa por ID
            reserva = form.save(commit=False)  # Crear instancia de reserva sin guardarla aún
            reserva.mesa = mesa  # Asignar la mesa a la reserva
            reserva.save()  # Guardar definitivamente en la base de datos
            # Recargar la página con las mesas y mostrar un mensaje de éxito
            return render(request, 'listarmesas.html', {
                'mesas': mesas,
                'form': ReservaForm(),  # Formulario vacío para siguiente reserva
                'success_message': f'Reserva creada para la mesa {mesa.identificador}.',
            })
    else:
        form = ReservaForm()  # Formulario vacío para la reserva

    return render(request, 'listarmesas.html', {
        'mesas': mesas,
        'form': form,
    })


def gestionmesas(request):
    """
    Vista unificada para gestionar mesas y reservaciones (crear, actualizar, eliminar).
    """
    if not request.user.is_staff:
        return render(request, '403.html', status=403)

    # Recuperar parámetros para determinar acción
    action = request.GET.get('action')  # acciones: create, update, delete
    type = request.GET.get('type')  # modelo: mesa, reserva
    object_id = request.GET.get('id')  # ID del objeto

    # Diccionario para manejar dinámicamente los modelos y formularios
    modelos = {
        'mesa': (Mesa, MesaForm),
        'reserva': (Reserva, ReservaForm),
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
                return redirect('gestionmesas')

        # Actualizar un registro existente
        elif action == 'update' and object_id:
            objeto = get_object_or_404(model, id=object_id)
            if request.method == 'POST':
                form = form_class(request.POST, instance=objeto)
                if form.is_valid():
                    form.save()
                    return redirect('gestionmesas')
            else:
                form = form_class(instance=objeto)

        # Eliminar un registro existente
        elif action == 'delete' and object_id:
            objeto = get_object_or_404(model, id=object_id)
            objeto.delete()
            return redirect('gestionmesas')

    # Listar todos los registros
    mesas = Mesa.objects.all()
    reservas = Reserva.objects.all()

    return render(request, 'gestionmesas.html', {
        'mesas': mesas,
        'reservas': reservas,
        'form': form,
        'objeto': objeto,
        'action': action,
        'type': type,
    })

def ubicacion(request):
    return render(request,'ubicacion.html',)

def paneladmin(request):
    return render(request, 'paneladmin.html')

