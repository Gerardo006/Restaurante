"""
URL configuration for Restaurante project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import pedidos.views
from mesas import views as mesas_views
from menus import views as menus_views
from inventario import views as inventario_views
from mesas.views import ubicacion
from pedidos import views
from mesas.views import enviar_mensaje_api
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', mesas_views.home, name='home'),

    path('menu/', menus_views.menus, name='menus'),

    path('menuvista/', menus_views.menuvista, name='menuvista'),

    path('inventario/', inventario_views.inventario, name='inventario'),

    path('inventariovista/', inventario_views.inventariovista, name='inventariovista'),

    path('gestionarmenus/', menus_views.gestionarmenus, name='gestionarmenus'),

    path('realizarpedido/', views.realizarpedido, name='realizarpedido'),

    path('crearmesas/', mesas_views.crearmesas, name='crearmesas'),

    path('listarmesas/', mesas_views.listarmesas, name='listarmesas'),

    path('gestionmesas/', mesas_views.gestionmesas, name='gestionmesas'),

    path('gestionpedidos/', views.gestionpedidos, name='gestionpedidos'),

    path('ubicacion/', mesas_views.ubicacion, name='ubicacion'),

    path('panel/', mesas_views.paneladmin, name='paneladmin'),

path('api/enviar/', enviar_mensaje_api, name='enviar_mensaje_api'),



]
