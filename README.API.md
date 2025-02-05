# API-Menu-Board

INTEGRANTES:

* Miguel Veintimilla
* Ariana Cordova
* Cristhian Davila
* Gerardo Naula


# IMPLEMENTACION:

![Captura de pantalla 2025-02-04 002757](https://github.com/user-attachments/assets/a85651c4-d5b0-49f1-8449-544be24373a5)



## Documentación
# Implementación de Google Maps API

## Descripcion del Proyecto

Este proyecto integra la API de Google Maps para proporcionar a los usuarios una funcionalidad que les permite visualizar la ruta desde su ubicación actual hasta un destino predefinido.

La Implementación de esta permite:

- Mostrar un mapa interactivo dentro de la página web.
- Identificar la ubicación actual del usuario mediante geolocalización.
- Calcular y mostrar la mejor ruta al destino.
- Agregar un marcador visual para indicar el destino.

## Funcionalidad agregada

La API de Google Maps permite a los usuarios obtener direcciones y ver la mejor ruta desde su ubicación hasta un punto específico. 

La funcionalidad se basa en:

- **Geolocalización:** Determina la ubicación actual del usuario con navigator.geolocation.getCurrentPosition.

- **Mapa interactivo:** Se crea y muestra un mapa con google.maps.Map.

- **Marcadores:** Se señala el destino con google.maps.Marker.

- **Cálculo de rutas:** Se utiliza google.maps.DirectionsService y google.maps.DirectionsRenderer para trazar la ruta entre la ubicación del usuario y el destino.

## Implementación

Requisitos previos a tomar en cuenta para que el codigo se pueda ejecutar:

- Una clave de API de Google Maps, obtenida desde Google Cloud Console.
- Un proyecto en Django donde se almacenen los archivos estáticos.

### Estructura del código

### HTML

1. Se cargan los recursos estaticos (static)

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/ubicacion.css' %}">
```

2. Contenedor principal:

```html
<div class="container">
    <div id="map"></div>
    <div class="image-container">
        <img src="{% static 'images/resubi.png' %}" alt="Imagen del destino">
    </div>
</div>
```
3. Boton de regreso:

```html
<a href="{% url 'home' %}" class="back-button">Regresar</a>
```

### Javascript

1. Inicializar el mapa y marcador

```html
function initMap() {
    const destination = { lat: -4.0329396, lng: -79.2051226 };
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 8,
        center: destination,
    });
    new google.maps.Marker({
        position: destination,
        map: map,
        title: "Destino",
    });
}
```

2. Obtener Ubicación del usuario

```html
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
        (position) => {
            const currentLocation = {
                lat: position.coords.latitude,
                lng: position.coords.longitude,
            };

```

3. Calcular la ruta

```html
const directionsService = new google.maps.DirectionsService();
const directionsRenderer = new google.maps.DirectionsRenderer({ map: map });

directionsService.route(
    {
        origin: currentLocation,
        destination: destination,
        travelMode: google.maps.TravelMode.DRIVING,
    },
    (response, status) => {
        if (status === "OK") {
            directionsRenderer.setDirections(response);
        } else {
            console.error("Error al obtener la ruta. Estado:", status);
        }
    }
);
```

4. Cargar el script del API de Google Maps en el HTML.

```html
<script async src="https://maps.googleapis.com/maps/api/js?key=TU_API_KEY&callback=initMap"></script>
```

## Uso de APIs y Librerías Estándar

## Criterio

### Integración de API
- Google Maps API se utiliza para la geolocalización y cálculo de rutas.

### Documentación clara
- Se explica cómo se estructura e implementa la funcionalidad.

### Eficiencia
- La API optimiza el cálculo de rutas y la interacción del usuario.

## Instrucciones para Ejecutar el Proyecto

1. Agregar la clave de API en el archivo HTML en la línea:
   ```html
   <script async src="https://maps.googleapis.com/maps/api/js?key=TU_API_KEY&callback=initMap"></script>
   ```
2. Asegurar que los archivos estáticos (`ubicacion.css`, `resubi.png`) estén ubicados en la carpeta `static` de Django.
3. Ejecutar el servidor Django:
   ```sh
   python manage.py runserver
   ```
4. Acceder a la URL donde esté alojada la página para visualizar el mapa interactivo.


# OPEN AI

Es una interfaz de programación de aplicaciones que permite acceder a modelos de inteligencia artificial avanzados, como GPT-4, GPT-3.5, DALL·E, CLAUDE y otros. Estos modelos están diseñados para tareas de procesamiento de lenguaje natural (NLP), generación de texto, resolución de problemas, traducción, y más. En el contexto de una aplicación de restaurantes, la API de OpenAI puede ser utilizada para mejorar la interacción con los clientes, automatizar tareas y generar contenido personalizado.

![Captura de pantalla 2025-02-04 161113](https://github.com/user-attachments/assets/5ef48e51-10fe-4461-b419-2ac392c17318)



# Funcionalidades Principales:

La API de OpenAI ofrece una amplia gama de funcionalidades que pueden ser útiles para una aplicación de restaurantes:

a. Generación de Texto

•	Descripción: Permite generar texto coherente y contextualmente relevante.
•	Casos de Uso en Restaurantes:
Creación automática de descripciones de platos para el menú.
Generación de respuestas automatizadas a preguntas frecuentes de los clientes (FAQ).
Creación de contenido para promociones, ofertas especiales o publicidad.

b. Asistencia Virtual y Chatbots

•	Descripción: Puede utilizarse para crear chatbots inteligentes que interactúen con los clientes.
•	Casos de Uso en Restaurantes:
Atención al cliente automatizada (reservas, consultas sobre menús, horarios, etc.).
Recomendaciones personalizadas de platos basadas en las preferencias del cliente.
Asistencia en la toma de pedidos a través de chat.

c. Traducción de Idiomas

•	Descripción: Traduce texto entre múltiples idiomas.
•	Casos de Uso en Restaurantes:
Ofrecer menús en varios idiomas para turistas o clientes extranjeros.
Comunicación con clientes que hablan otros idiomas.

d. Resumen de Texto

•	Descripción: Resume textos largos en versiones más cortas y concisas.
•	Casos de Uso en Restaurantes:
Resumir reseñas de clientes para identificar tendencias o problemas comunes.
Crear resúmenes de noticias o artículos relacionados con la industria de restaurantes.

e. Generación de Ideas y Contenido Creativo

•	Descripción: Ayuda a generar ideas creativas para menús, promociones o eventos.
•	Casos de Uso en Restaurantes:
Crear nombres atractivos para nuevos platos o bebidas.
Generar ideas para eventos temáticos o noches especiales.

# Requisitos para Usar la API de OpenAI

Para utilizar la API de OpenAI, es necesario cumplir con los siguientes requisitos:
1.	Registro y Clave API:
Crear una cuenta en OpenAI.
Obtener una clave API desde el panel de control de OpenAI.
2.	Configuración del Entorno:
Instalar la biblioteca oficial de OpenAI (disponible para Python, Node.js, etc.).
pip install openai
1.	Facturación:
La API de OpenAI es un servicio de pago por uso. Es necesario configurar un método de pago en la plataforma de OpenAI.
El costo depende del modelo utilizado y del número de tokens procesados (1 token ≈ 4 caracteres en inglés).
2.	Límites de Uso:
Los planes gratuitos tienen límites de uso (por ejemplo, 5 USD de crédito inicial).
Los planes de pago permiten un mayor volumen de solicitudes.
Limitaciones
Aunque la API de OpenAI es muy poderosa, tiene algunas limitaciones que debes considerar:
1.	Costos:
El uso intensivo de la API puede generar costos elevados, especialmente si se utiliza para tareas que requieren muchos tokens (como la generación de texto largo).
2.	Precisión:
Aunque los modelos son muy avanzados, pueden generar respuestas incorrectas o poco precisas en algunos casos. Es importante supervisar y validar las salidas.
3.	Dependencia de Internet:
La API requiere una conexión a Internet para funcionar, lo que puede ser un problema en áreas con conectividad limitada.
4.	Privacidad:
Los datos enviados a la API se procesan en servidores de OpenAI. Asegúrate de cumplir con las regulaciones de privacidad de datos (como GDPR) si manejas información sensible

# Propuesta de Integración en MenuBoard

Objetivo:

Integrar la API de OpenAI en MenuBoard para automatizar la generación de descripciones de platos, mejorar la atención al cliente mediante un chatbot y ofrecer recomendaciones personalizadas.

Beneficios:

•	Ahorro de Tiempo: Automatiza tareas repetitivas como la creación de contenido.
•	Mejora de la Experiencia del Usuario: Ofrece respuestas rápidas y personalizadas a los clientes.
•	Innovación: Incorpora inteligencia artificial para diferenciar tu aplicación de la competencia.

Pasos para la Integración:

1.	Registro en OpenAI: Obtén tu clave API.
2.	Configuración del Backend: Implementa endpoints para interactuar con la API.
3.	Desarrollo del Frontend: Crea interfaces para mostrar las respuestas generadas por OpenAI.
4.	Pruebas y Validación: Asegúrate de que las respuestas sean precisas y útiles.







