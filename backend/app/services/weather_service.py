import requests
from app.config import Config

URL_WEATHER = "https://weather.googleapis.com/v1/currentConditions:lookup"
URL_FORECAST = "https://weather.googleapis.com/v1/forecast:lookup"

def get_current_conditions(lat: float, lng: float):
    params = {
        "key": Config.GOOGLE_API_KEY,
        "location.latitude": lat,
        "location.longitude": lng
    }

    resp = requests.get(URL_WEATHER, params=params)

    if resp.status_code != 200:
        return None

    data = resp.json()

    return {
        "temperature": data.get("temperature"),
        "weather_condition": data.get("weatherCondition"),
        "humidity": data.get("humidity")
    }


def get_forecast(lat: float, lng: float, days: int = 5):
    params = {
        "key": Config.GOOGLE_API_KEY,
        "location.latitude": lat,
        "location.longitude": lng,
        "days": days
    }

    try:
        resp = requests.get(URL_FORECAST, params=params)
        resp.raise_for_status()
        data = resp.json()

        forecasts = []

        for day in data.get("dailyForecasts", []):
            forecasts.append({
                "date": day.get("date"),
                "max_temp": day.get("temperatureMax", {}).get("value"),
                "min_temp": day.get("temperatureMin", {}).get("value"),
                "condition": day.get("weatherCondition", {}).get("type")
            })

        return forecasts

    except requests.exceptions.RequestException:
        return None