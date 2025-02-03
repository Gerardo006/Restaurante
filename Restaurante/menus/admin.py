from django.contrib import admin
from .models import Menu, Categoria, Producto

class CategoriaInline(admin.TabularInline):
    model = Categoria
    extra = 1
    fields = ('nombre',)

# Personalizacion de la administracion del modelo Menu
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado')
    list_filter = ('estado',)
    search_fields = ('nombre',)



# Personalización de la administración del modelo Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'menu')
    list_filter = ('menu',)
    search_fields = ('nombre',)


# Personalización de la administración del modelo Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'categoria')
    search_fields = ('nombre', 'descripcion')

