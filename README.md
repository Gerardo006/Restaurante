# Restaurante
Gestion de restaurantes

# INTEGRANTES: 

* Miguel Veintimilla
* Ariana Cordova
* Cristhian Davila
* Gerardo Naula


# Documentación del Proyecto de Restaurante (GUI)


# Introducción

Este documento describe el proceso de diseño e implementación de la interfaz de usuario (UI) para un sistema de gestión de restaurantes. La interfaz fue diseñada para ser intuitiva, eficiente y fácil de usar, permitiendo a los usuarios gestionar menús, pedidos, reservas y empleados de manera efectiva.

Como se puede observar en la siguiente imagen:


![image](https://github.com/user-attachments/assets/d348ee09-1257-4a91-923f-2888c2429647)


Modulos:


# Modulo de Mesas y Reservaciones:

Este módulo administra la disponibilidad y el uso de las mesas en el restaurante. Cada mesa puede tener distintos estados, como disponible, ocupada o reservada. Los clientes pueden realizar reservas indicando la fecha y hora, además de identificar cada mesa según su número de asientos y ubicación dentro del establecimiento. Al recibir a un cliente, se le puede asignar una mesa, la cual deberá ser liberada una vez finalizado su uso para permitir su reutilización. Tanto los clientes como el personal del restaurante pueden modificar o cancelar las reservas según sea necesario. Este módulo mantiene una interacción directa con el usuario.

![image](https://github.com/user-attachments/assets/3441fb9b-dec0-465a-8b14-4b0c75635994)


# Modulo de Pedidos:

El módulo de pedidos facilita la administración de las órdenes de los clientes, desde su registro hasta su entrega y pago. Cada orden puede incluir uno o varios productos del menú, con la opción de añadir o retirar artículos mientras no haya sido procesada. Además, el sistema permite ajustar las cantidades de los productos dentro del pedido y actualizar su estado en tiempo real. Este módulo mantiene una interacción constante con el usuario.


![image](https://github.com/user-attachments/assets/dccf55e2-80ea-4c86-bb74-302cb8bdffa0)



# Modulo de Menu y Productos:

Este módulo administra los platos y productos disponibles en el restaurante. Cada artículo cuenta con características como nombre, descripción, categoría, precio y estado de disponibilidad. El menú se estructura por categorías, y el sistema permite incorporar nuevos productos, editar los existentes o eliminarlos según sea necesario.


![image](https://github.com/user-attachments/assets/c7a11c1e-4cc0-432e-acaa-d78ee6998451)


# Modulo de Inventario.


El módulo de inventario facilita la administración de los insumos y productos esenciales para la elaboración de los platillos del restaurante. Cada insumo se encuentra registrado con su nombre, cantidad disponible y unidad de medida. El sistema permite registrar nuevas entradas y controlar las salidas de insumos, además de generar alertas cuando los niveles sean bajos o se agoten. Su acceso está restringido únicamente al administrador


![image](https://github.com/user-attachments/assets/e856f9c6-f77c-4fd4-aaf8-b1a1e0b63260)


# Modulo de Informes y Estadistica:

Este módulo proporciona información sobre el rendimiento del restaurante mediante reportes y estadísticas presentadas en gráficos interactivos y archivos PDF. Los datos incluyen los productos más vendidos, la mesa con mayor uso, el desempeño del personal y las ventas totales. La información se genera con base en un rango de fechas definido por el administrador.


![image](https://github.com/user-attachments/assets/db5fbbc8-f2ab-40b3-8a1b-ea14325d2516)


# Modulo de Facturacion:

Este módulo permite la emisión de facturas, calculando automáticamente el total del pedido, incluyendo impuestos y descuentos, además de registrar el método de pago utilizado. También almacena un historial de todas las facturas generadas. El acceso a este módulo está restringido exclusivamente al administrador.


# Conclusión:

Al realizar este proyecto obtuvimos una experiencia entendedora que nos permitió aplicar y consolidar los conocimientos adquiridos a lo largo de la tercera unidad. Aprendimos la importancia de una planificación cuidadosa, la necesidad de pruebas rigurosas y cómo resolver problemas inesperados durante el desarrollo. La integración de múltiples componentes como la interfaz, API externa fue un desafío, pero también una oportunidad para mejorar nuestras habilidades técnicas y de resolución de problemas.


