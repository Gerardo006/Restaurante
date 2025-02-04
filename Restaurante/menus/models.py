from django.db import models



class Menu(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre

    def activar_menu(self) -> None:
        self.estado = True
        self.save()

    def desactivar_menu(self) -> None:
        self.estado = False
        self.save()


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='categorias')

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre





