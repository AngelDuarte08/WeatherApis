import requests
from app.config import Config

URL_AIR = "https://airquality.googleapis.com/v1/currentConditions:lookup"

def get_air_quality(lat: float, lng: float):
    url = f"{URL_AIR}?key={Config.GOOGLE_API_KEY}"

    body = {
        "location": {
            "latitude": lat,
            "longitude": lng
        }
    }

    resp = requests.post(url, json=body)
    data = resp.json()

    if resp.status_code != 200 or "indexes" not in data:
        return None

    idx = data["indexes"][0]

    return {
        "aqi": idx.get("aqi"),
        "category": idx.get("category")
    }
