import requests
import pandas as pd
import geopandas as gpd

code_commune="01450"
size = 100
api_root="https://koumoul.com/data-fair/api/v1/datasets/dpe-france/lines"
url_api = f"{api_root}?page=1&after=10&format=json&q_mode=simple&qs=code_insee_commune_actualise" + "%3A%22" + f"{code_commune}" + "%22" + f"&size={size}&select=" + "%2A&sampling=neighbors"

#Function
def get_dpe_from_url(url):
    req = requests.get(url)
    wb = req.json()
    df = pd.json_normalize(wb["results"])

    #Récupération des données géographique
    dpe = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude, crs=4326))
    dpe = dpe.dropna(subset=["longitude", "latitude"])
    return dpe
dpe = get_dpe_from_url(url_api)
print(dpe.head(2))