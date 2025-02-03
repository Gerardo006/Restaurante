from django import forms
from .models import Categoria, Insumo, MovimientoInventario


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'inventario']


class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'categoria', 'cantidad_disponible', 'unidad_medida', 'nivel_reorden']


class MovimientoInventarioForm(forms.ModelForm):
    class Meta:
        model = MovimientoInventario
        fields = ['insumo', 'tipo', 'cantidad', 'descripcion']