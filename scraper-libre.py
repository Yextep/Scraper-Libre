import requests
import json
import os
from bs4 import BeautifulSoup
from openpyxl import Workbook
import pandas as pd

# Tu API key de ScraperAPI
api_key = 'AQUÍ-VA-TU-API'

# Función para solicitar la URL al usuario
def get_target_url():
    return input('Por favor, ingresa la URL de la página de MercadoLibre que deseas scrapear: ')

# Función para realizar la solicitud y extraer los datos
def scrape_data(target_url):
    # Parámetros para la solicitud a ScraperAPI
    payload = {
        'api_key': api_key,
        'url': target_url,
        'autoparse': 'true'
    }

    # Realizar la solicitud GET a través de ScraperAPI
    response = requests.get('https://api.scraperapi.com/', params=payload)
    content = response.text

    # Parsear el contenido HTML de la respuesta
    soup = BeautifulSoup(content, 'html.parser')

    # Lista para almacenar la información de los productos
    products = []

    # Encontrar todos los contenedores que contienen información de los productos
    product_containers = soup.find_all('li', class_='ui-search-layout__item')

    # Verificar si se encontraron productos
    if not product_containers:
        print("No se encontraron productos. Verifica los selectores HTML.")
        return products
    else:
        print(f"Se encontraron {len(product_containers)} productos.")

    # Extraer información de cada producto
    for container in product_containers:
        try:
            # Extraer el enlace del producto
            link_tag = container.find('a', class_='ui-search-link')
            link = link_tag['href'] if link_tag else 'Enlace no disponible'

            # Extraer el nombre del producto
            name_tag = container.find('h2', class_='ui-search-item__title')
            name = name_tag.get_text(strip=True) if name_tag else 'Nombre no disponible'

            # Extraer el precio del producto
            price_tag = container.find('span', class_='andes-money-amount__fraction')
            price = price_tag.get_text(strip=True) if price_tag else 'Precio no disponible'

            # Agregar la información del producto a la lista
            products.append({
                'link': link,
                'name': name,
                'price': price
            })
        except AttributeError as e:
            # Mostrar el error para depuración
            print(f"Error al extraer datos de un producto: {e}")
            continue

    return products

# Función para cargar los datos previos desde un archivo JSON
def load_previous_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

# Función para guardar los datos ordenados en JSON y XLSX
def save_data(products, json_path, xlsx_path):
    # Ordenar los productos por precio de menor a mayor
    sorted_products = sorted(products, key=lambda x: float(x['price'].replace('.', '').replace(',', '.')))

    # Guardar la información en un archivo JSON
    with open(json_path, 'w', encoding='utf-8') as file:
        json.dump(sorted_products, file, ensure_ascii=False, indent=4)

    print(f"Datos guardados en '{json_path}'")

    # Crear un DataFrame con los productos
    df = pd.DataFrame(sorted_products)

    # Guardar el DataFrame en el archivo XLSX
    df.to_excel(xlsx_path, index=False)

    print(f"Datos guardados en '{xlsx_path}'")

# Crear una carpeta si no existe
if not os.path.exists('resultados'):
    os.makedirs('resultados')

# Ruta de los archivos JSON y XLSX
json_path = 'resultados/productos.json'
xlsx_path = 'resultados/productos.xlsx'

# Cargar los datos previos
previous_data = load_previous_data(json_path)

# Obtener la URL de la página a scrapear
target_url = get_target_url()

# Realizar el scrapeo de datos
new_data = scrape_data(target_url)

# Acumular los datos
all_data = previous_data + new_data

# Guardar los datos acumulados
save_data(all_data, json_path, xlsx_path)
