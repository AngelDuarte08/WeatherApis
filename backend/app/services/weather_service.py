import requests
from app.config import Config
from typing import List, Optional

URL_WEATHER = "https://weather.googleapis.com/v1/currentConditions:lookup"
URL_FORECAST = "https://weather.googleapis.com/v1/forecast/hours:lookup"

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


def get_forecast(lat: float, lng: float) -> Optional[List[dict]]:
    params = {
        "key": Config.GOOGLE_API_KEY,
        "location.latitude": lat,
        "location.longitude": lng
    }

    try:
        resp = requests.get(URL_FORECAST, params=params, timeout=10)
        resp.raise_for_status()

        data = resp.json()
        hourly_data = data.get("forecastHours", [])

        forecasts = []

        for hour in hourly_data:
            # Construir hora legible
            display = hour.get("displayDateTime", {})
            year = display.get("year")
            month = display.get("month")
            day = display.get("day")
            hours = display.get("hours")

            formatted_time = (
                f"{year}-{month:02d}-{day:02d} {hours:02d}:00"
                if all(v is not None for v in [year, month, day, hours])
                else "Sin hora"
            )

            forecasts.append({
                "time": formatted_time,
                "temperature": hour.get("temperature", {}).get("degrees", 0),
                "condition": hour.get("weatherCondition", {})
                                .get("description", {})
                                .get("text", "N/A"),
                "isDaytime": hour.get("isDaytime", False)
            })

        return forecasts

    except requests.exceptions.RequestException as e:
        print("Error en la petición a la API:", e)
        return None

    except Exception as e:
        print("Error inesperado en get_forecast:", e)
        return None