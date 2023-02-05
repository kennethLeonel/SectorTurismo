import requests
import pandas as pd
import geopandas as gpd

# # Hacer una solicitud HTTP para descargar los datos del sitio web
# url = "https://ejemplo.com/datos.xlsx"
# response = requests.get(url)

# # Verificar si la solicitud fue exitosa
# if response.status_code == 200:
#     # Guardar los datos en un archivo en disco
#     open("datos.xlsx", "wb").write(response.content)

#     # Leer los datos en un DataFrame de pandas
#     df = pd.read_excel("datos.xlsx")
#     print(df.head())
# else:
#     print("No se pudieron descargar los datos")

# # Para descargar un archivo GeoJSON:
# url = "https://ejemplo.com/datos.geojson"
# response = requests.get(url)

# # Verificar si la solicitud fue exitosa
# if response.status_code == 200:
#     # Guardar los datos en un archivo en disco
#     open("datos.geojson", "wb").write(response.content)

#     # Leer los datos en un GeoDataFrame de geopandas
#     gdf = gpd.read_file("datos.geojson")
#     print(gdf.head())
# else:
#     print("No se pudieron descargar los datos")

# Para descargar un archivo Json: 
url = "https://www.datos.gov.co/resource/thwd-ivmp.json?$query=SELECT%0A%20%20%60ano%60%2C%0A%20%20%60mes%60%2C%0A%20%20%60codigo_rnt%60%2C%0A%20%20%60cod_mun%60%2C%0A%20%20%60cod_dpto%60%2C%0A%20%20%60estado_rnt%60%2C%0A%20%20%60razon_social_establecimiento%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60municipio1%60%2C%0A%20%20%60categoria1%60%2C%0A%20%20%60sub_categoria1%60%2C%0A%20%20%60habitaciones1%60%2C%0A%20%20%60camas1%60%2C%0A%20%20%60num_emp1%60"
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Guardar los datos en un archivo en disco
    open("datos.json", "wb").write(response.content)

    # Leer los datos en un DataFrame de pandas
    df = pd.read_json("datos.json")
    print(df.head())
else:
    print("No se pudieron descargar los datos")
    
