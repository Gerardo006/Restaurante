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
from mesas import views as mesas_views
from menus import views as menus_views
from inventario import views as inventario_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', mesas_views.home, name='home'),

    path('menu/', menus_views.menus, name='menus'),

    path('menuvista/', menus_views.menuvista, name='menuvista'),

    path('inventario/', inventario_views.inventario, name='inventario'),

    path('inventariovista/', inventario_views.inventariovista, name='inventariovista'),

    path('gestionarmenus/', menus_views.gestionarmenus, name='gestionarmenus'),
]
