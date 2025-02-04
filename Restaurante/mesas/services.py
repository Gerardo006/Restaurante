import requests
from django.conf import settings


def consumir_api_claude3(mensaje, web_access=False):
    """
    Función para enviar una solicitud POST a la API Claude3.
    Args:
        mensaje (str): El mensaje que quieres enviar.
        web_access (bool): Habilitar o deshabilitar acceso web en la API.

    Returns:
        dict: Respuesta de la API en formato JSON.
    """
    url = f"https://{settings.RAPIDAPI_HOST}/claude3"  # Endpoint de la API
    headers = {
        "X-Rapidapi-Key": settings.RAPIDAPI_KEY,
        "X-Rapidapi-Host": settings.RAPIDAPI_HOST,
        "Content-Type": "application/json"
    }
    payload = {
        "messages": [{"role": "user", "content": mensaje}],
        "web_access": web_access
    }

    # Realizar la solicitud POST
    response = requests.post(url, headers=headers, json=payload)

    # Manejar la respuesta
    if response.status_code == 200:  # Solicitud exitosa
        return response.json()  # Convertir a diccionario Python
    else:
        # Manejo de errores
        return {"error": f"Error {response.status_code}: {response.text}"}