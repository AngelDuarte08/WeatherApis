from app.services.google_maps_service import get_coordinates
from app.services.weather_service import get_current_conditions, get_forecast # Agregamos get_forecast
from app.services.air_quality_service import get_air_quality

def procesar_mensaje_sms(texto_recibido):
    comando = texto_recibido.lower().strip()
    if " en " in comando:
        partes = comando.split(" en ")
        accion = partes[0]
        ciudad = partes[1]
    else:
        return "Hola! Prueba diciendo: 'clima en [ciudad]', 'aire en [ciudad]' o 'pronostico en [ciudad]'"

    try:
        coords = get_coordinates(ciudad)
        if not coords:
            return f"Lo siento, no pude encontrar la ubicación de {ciudad}."

        # 1. Clima Actual
        if "clima" in accion:
            res = get_current_conditions(coords["lat"], coords["lng"])
            temp = res['temperature']['degrees']
            cond = res['weather_condition']['description']['text']
            return f"El clima en {ciudad.capitalize()} es de {temp}°C con {cond}."

        # 2. Calidad del Aire
        elif "aire" in accion:
            res = get_air_quality(coords["lat"], coords["lng"])
            return f"Calidad del aire en {ciudad.capitalize()}: {res['category']} (AQI: {res['aqi']})."
        
        # 3. Pronóstico
        elif "pronostico" in accion or "pronóstico" in accion:
            res = get_forecast(coords["lat"], coords["lng"])
            # Tomamos los datos de la primera hora del pronóstico para el SMS
            proxima_hora = res[0] 
            tiempo = proxima_hora['time'].split(" ")[1] # Extraemos solo la hora
            temp_f = proxima_hora['temperature']
            cond_f = proxima_hora['condition']
            
            return f"Pronóstico para {ciudad.capitalize()}: A las {tiempo} se esperan {temp_f}°C con cielo {cond_f}."

        # 4. Coordenadas
        elif "coordenadas" in accion:
            return f"{ciudad.capitalize()} está en: Lat {coords['lat']}, Lng {coords['lng']}."

        else:
            return "Comando no reconocido. Prueba con 'clima', 'aire', 'pronostico' o 'coordenadas'."

    except Exception as e:
        print(f"Error en chatbot: {e}")
        return "Ups, hubo un error al consultar los datos. Intenta más tarde."