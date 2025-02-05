from django.db import models


class Mesa(models.Model):
    numero = models.IntegerField(unique=True, verbose_name="Número de Mesa")
    capacidad = models.IntegerField(verbose_name="Capacidad")

    def __str__(self):
        return f"Mesa {self.numero}"

class Reservacion(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, verbose_name="Mesa Reservada")
    nombre_cliente = models.CharField(max_length=100, verbose_name="Nombre del Cliente")
    fecha = models.DateTimeField(verbose_name="Fecha y Hora de la Reservación")

    def __str__(self):
        return f"Reservación de {self.nombre_cliente} en {self.mesa}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Producto")
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    ESTADOS = [
        ('P', 'Pendiente'),
        ('R', 'En preparación'),
        ('S', 'Servido'),
        ('C', 'Pagado'),
    ]
    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Mesa")
    reservacion = models.ForeignKey(Reservacion, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Reservación")
    cliente = models.CharField(max_length=100, verbose_name="Nombre del Cliente", blank=True, null=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P', verbose_name="Estado del Pedido")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    actualizado_en = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    def __str__(self):
        return f"Pedido {self.id} - {self.get_estado_display()}"

    def monto_total(self):
        return sum(detalle.producto.precio * detalle.cantidad for detalle in self.detalles.all())

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles', verbose_name="Pedido")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    detalles = models.TextField(blank=True, null=True, verbose_name="Detalles Adicionales")

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} en {self.pedido}"

class HistorialPedido(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='historial', verbose_name="Pedido")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del Historial")
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto Total")

    def __str__(self):
        return f"Historial del Pedido {self.pedido.id} - {self.fecha}"

    def save(self, *args, **kwargs):
        # Calcula el monto total del pedido antes de guardar
        self.monto_total = self.pedido.monto_total()
        super().save(*args, **kwargs)