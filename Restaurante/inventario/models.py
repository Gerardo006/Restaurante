from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from typing import Any

class InventarioPrincipal(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    inventario = models.ForeignKey(InventarioPrincipal, on_delete=models.CASCADE, related_name='categorias')

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(args, kwargs)
        self.insumo_set = None

    def __str__(self):
        return self.nombre

class Insumo(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='insumos')
    cantidad_disponible = models.FloatField(default=0)
    unidad_medida = models.CharField(max_length=50)
    nivel_reorden = models.FloatField()

    def __str__(self):
        return f"{self.nombre} ({self.cantidad_disponible} {self.unidad_medida})"

class MovimientoInventario(models.Model):
    TIPO_MOVIMIENTO = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    ]
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, related_name='movimientos')
    tipo = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO)
    cantidad = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo.capitalize()} - {self.insumo.nombre} ({self.cantidad} {self.insumo.unidad_medida})"

@receiver(post_save, sender=MovimientoInventario)
def actualizar_inventario(instance, sender, **kwargs):
    if instance.tipo == 'entrada':
        instance.insumo.cantidad_disponible += instance.cantidad
    elif instance.tipo == 'salida':
        instance.insumo.cantidad_disponible -= instance.cantidad
    instance.insumo.save()

class ReporteConsumo(models.Model):
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad_consumida = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(args, kwargs)
        self.fecha_consumo = None

    def __str__(self):
        return f"{self.insumo.nombre}: {self.cantidad_consumida} {self.insumo.unidad_medida} ({self.fecha_inicio} - {self.fecha_fin})"

class ReporteInventario(models.Model):
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    inventario = models.ForeignKey(InventarioPrincipal, on_delete=models.CASCADE)

    def generar_reporte(self):
        insumos = Insumo.objects.filter(categoria__inventario=self.inventario)
        return [
            {
                "nombre": insumo.nombre,
                "cantidad_disponible": insumo.cantidad_disponible,
                "unidad_medida": insumo.unidad_medida,
                "nivel_reorden": insumo.nivel_reorden,
            }
            for insumo in insumos
        ]

    def __str__(self):
        return f"Reporte de Inventario - {self.inventario.nombre} ({self.fecha_generacion})"