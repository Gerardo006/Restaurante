import requests

# Configuración de la API
API_KEY = '4fa5b91f1fmsh13b9ef657d29004p1d2090jsn13d9ecbcbd92'  # Cambia esto con tu clave
BASE_URL = "https://food-recipes-with-images.p.rapidapi.com"
HEADERS = {
    "X-Rapidapi-Key": API_KEY,
    "X-Rapidapi-Host": "food-recipes-with-images.p.rapidapi.com",
}


def search_recipes(query, limit=10):
    """
    Busca recetas en la API según el término de búsqueda (query).
    """
    url = f"{BASE_URL}/?"  # Endpoint base de búsqueda
    params = {"q": query}  # Parámetro de búsqueda

    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code == 200:
        return response.json()  # Respuesta en formato JSON
    else:
        response.raise_for_status()  # Levanta un error si falla


def get_recipe_by_id(recipe_id):
    """
    Recupera detalles de una receta específica usando su ID.
    """
    url = f"{BASE_URL}/{recipe_id}"  # Endpoint para detalles de la receta
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()