# forms.py
from django import forms
from .models import Pedido  # Asegúrate de que el modelo Pedido está creado
from mesas.models import Mesa, Reserva
from menus.models import Producto

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido  # Usa tu modelo en caso de que este exista
        fields = ['identificador', 'producto', 'cliente', 'estado','detalles']
        # Sustituye por los campos reales del modelo tuyo

    mesa = forms.ModelChoiceField(
        queryset=Mesa.objects.all(),  # Trae todas las mesas existentes
        required=True,
        label="Seleccionar Mesa",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    reserva = forms.ModelChoiceField(
        queryset=Reserva.objects.all(),  # Todas las reservaciones disponibles
        required=False,  # En caso de que sea opcional
        label="Seleccionar Reserva",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )



