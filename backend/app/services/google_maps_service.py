import requests
from app.config import Config

URL_GEO = "https://maps.googleapis.com/maps/api/geocode/json"

def get_coordinates(direccion: str):
    params = {
        "address": direccion,
        "key": Config.GOOGLE_API_KEY
    }

    resp = requests.get(URL_GEO, params=params)
    geo_data = resp.json()

    if geo_data.get('status') != 'OK':
        return None

    result = geo_data['results'][0]
    location = result['geometry']['location']

    return {
        "lat": location['lat'],
        "lng": location['lng']
    }
