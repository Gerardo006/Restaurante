from django import forms
from .models import Mesa, Reserva


class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['identificador', 'numero_asientos','mesas_unidas', 'ubicacion', 'estado']  # Incluye los campos necesarios


class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ['cliente', 'cantidad_personas','fecha_reserva', 'horario_inicio', 'hora_reserva_finalizada']
        widgets = {
            'fecha_reserva': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'horario_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'hora_reserva_finalizada': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_reserva'].input_formats = ['%Y-%m-%dT%H:%M']
