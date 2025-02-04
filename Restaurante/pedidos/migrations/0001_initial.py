# Generated by Django 5.1.5 on 2025-02-02 02:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True, verbose_name='Número de Mesa')),
                ('capacidad', models.IntegerField(verbose_name='Capacidad')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Producto')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=10, unique=True, verbose_name='Identificador')),
                ('cliente', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre del Cliente')),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('R', 'En preparación'), ('S', 'Servido'), ('C', 'Pagado')], default='P', max_length=1, verbose_name='Estado del Pedido')),
                ('creado_en', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizado_en', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('detalles', models.TextField(blank=True, null=True, verbose_name='Detalles Adicionales')),
                ('mesa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pedidos.mesa', verbose_name='Mesa')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Historial')),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto Total')),
                ('pedido', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='historial', to='pedidos.pedido', verbose_name='Pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=100, verbose_name='Nombre del Cliente')),
                ('fecha', models.DateTimeField(verbose_name='Fecha y Hora de la Reservación')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.mesa', verbose_name='Mesa Reservada')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='reservacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pedidos.reservacion', verbose_name='Reservación'),
        ),
    ]
