# Scraper-Libre

Este script permite scrapear información de productos de una página de MercadoLibre y guardar los datos en archivos JSON y XLSX.
El script extrae información de productos, incluyendo el enlace, el nombre y el precio, desde una página de MercadoLibre proporcionada por el usuario. Los datos se ordenan por precio de menor a mayor y se guardan en dos formatos: JSON y XLSX.

# Requisitos

- Python 3.x
- [ScraperAPI](https://www.scraperapi.com/)
- Librerías de Python:
  - `requests`
  - `json`
  - `os`
  - `BeautifulSoup` de `bs4`
  - `openpyxl`
  - `pandas`

## Instalación de Librerías

Para instalar las librerías necesarias, puedes usar pip:

```sh
pip3 install -r requirements.txt
```

## Configuración de ScraperAPI

Para utilizar el script, necesitas una API key de ScraperAPI. Puedes registrarte y obtener una en [ScraperAPI](https://www.scraperapi.com/).

## Uso

1. Clona este repositorio o descarga el archivo del script.
2. Abre el archivo del script en tu editor de texto favorito.
3. Encuentra la siguiente línea y reemplaza `'AQUÍ-VA-TU-API'` con tu propia API key de ScraperAPI:

    ```python
    api_key = 'AQUÍ-VA-TU-API'
    ```

4. Guarda los cambios.
5. Ejecuta el script:

    ```sh
    python3 tu_script.py
    ```

6. Ingresa la URL de la página de MercadoLibre que deseas scrapear cuando se te solicite.

## Estructura del Código

- `get_target_url()`: Solicita la URL de la página de MercadoLibre al usuario.
- `scrape_data(target_url)`: Realiza la solicitud a ScraperAPI, parsea el contenido HTML y extrae la información de los productos.
- `load_previous_data(file_path)`: Carga los datos previos desde un archivo JSON si existe.
- `save_data(products, json_path, xlsx_path)`: Guarda los datos ordenados en archivos JSON y XLSX.
- `if __name__ == "__main__"`: Verifica si la carpeta `resultados` existe, carga datos previos, obtiene la URL objetivo, realiza el scraping y guarda los datos acumulados.

## Notas

- Verifica los selectores HTML utilizados en el script (`'ui-search-layout__item'`, `'ui-search-link'`, `'ui-search-item__title'`, `'andes-money-amount__fraction'`) ya que pueden cambiar con el tiempo.
- En caso de error en la extracción de datos, se mostrará un mensaje de error para depuración.

## Contribución

Las contribuciones son bienvenidas. Si deseas mejorar el script o añadir nuevas funcionalidades, no dudes en enviar un pull request.
