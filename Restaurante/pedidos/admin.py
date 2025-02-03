from django.contrib import admin
from .models import Mesa, Reservacion, Producto, Pedido, HistorialPedido


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'capacidad')
    search_fields = ('numero',)


@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('mesa', 'nombre_cliente', 'fecha')
    list_filter = ('fecha', 'mesa')
    search_fields = ('nombre_cliente',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion')
    search_fields = ('nombre',)
    list_filter = ('precio',)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('identificador','producto', 'mesa','reservacion', 'cliente', 'estado', 'creado_en', 'actualizado_en','detalles',)
    list_filter = ('estado', 'creado_en')
    readonly_fields = ('creado_en', 'actualizado_en')


@admin.register(HistorialPedido)
class HistorialPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'fecha', 'monto_total')
    list_filter = ('fecha',)
    search_fields = ('pedido__identificador',)
    readonly_fields = ('monto_total',)



