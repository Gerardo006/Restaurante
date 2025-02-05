from django.contrib import admin

from .models import DetallePedido, Mesa, Pedido, Producto, Reservacion, HistorialPedido


# Configuración del admin para el modelo Mesa
@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'capacidad')  # Columnas mostradas en la lista
    search_fields = ('numero',)  # Campos de búsqueda
    list_filter = ('capacidad',)  # Filtros laterales

# Configuración del admin para el modelo Reservacion
@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('mesa', 'nombre_cliente', 'fecha')  # Columnas mostradas en la lista
    search_fields = ('nombre_cliente', 'mesa__numero')  # Campos de búsqueda
    list_filter = ('fecha', 'mesa')  # Filtros laterales
    date_hierarchy = 'fecha'  # Navegación por fechas

# Configuración del admin para el modelo Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')  # Columnas mostradas en la lista
    search_fields = ('nombre',)  # Campos de búsqueda
    list_filter = ('precio',)  # Filtros laterales

# Configuración del admin para el modelo DetallePedido (Inline)
class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1  # Número de formularios vacíos para agregar detalles
    # Personaliza los campos que se muestran en el inline
    fields = ('producto', 'cantidad', 'detalles')
    # Filtra los productos disponibles en el dropdown
    raw_id_fields = ('producto',)  # Permite buscar productos en un popup
    autocomplete_fields = ('producto',)  # Habilita la búsqueda de productos

# Configuración del admin para el modelo Pedido
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'mesa', 'cliente', 'estado', 'creado_en', 'monto_total')  # Columnas mostradas en la lista
    search_fields = ('cliente', 'mesa__numero')  # Campos de búsqueda
    list_filter = ('estado', 'creado_en')  # Filtros laterales
    inlines = [DetallePedidoInline]  # Incluye los detalles del pedido

    # Método personalizado para mostrar el monto total en el admin
    def monto_total(self, obj):
        return f"${obj.monto_total()}"

    monto_total.short_description = 'Monto Total'

    # Método personalizado para mostrar el monto total en el admin
    def monto_total(self, obj):
        return f"${obj.monto_total()}"
    monto_total.short_description = 'Monto Total'

# Configuración del admin para el modelo HistorialPedido
@admin.register(HistorialPedido)
class HistorialPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'fecha', 'monto_total')  # Columnas mostradas en la lista
    search_fields = ('pedido__cliente',)  # Campos de búsqueda
    list_filter = ('fecha',)  # Filtros laterales
    date_hierarchy = 'fecha'  # Navegación por fechas

