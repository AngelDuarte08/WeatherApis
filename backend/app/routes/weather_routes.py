from flask import Blueprint, request, jsonify
from app.services.weather_service import get_current_conditions, get_forecast
from app.services.google_maps_service import get_coordinates

weather_bp = Blueprint("weather", __name__)

@weather_bp.route("/current-weather", methods=["POST"])
def current_weather():
    data = request.get_json()
    ciudad = data.get("ciudad")

    if not ciudad:
        return jsonify({"error": "Ciudad requerida"}), 400

    coords = get_coordinates(ciudad)

    if not coords:
        return jsonify({"error": "No se encontraron coordenadas"}), 404

    result = get_current_conditions(coords["lat"], coords["lng"])

    if not result:
        return jsonify({"error": "No se pudo obtener clima actual"}), 500

    return jsonify({
        "ciudad": ciudad,
        "lat": coords["lat"],
        "lng": coords["lng"],
        "weather": result
    }), 200

@weather_bp.route("/forecast", methods=["POST"])
def forecast():
    data = request.get_json()
    ciudad = data.get("ciudad")

    if not ciudad:
        return jsonify({"error": "Ciudad requerida"}), 400

    coords = get_coordinates(ciudad)

    if not coords:
        return jsonify({"error": "No se encontraron coordenadas"}), 404

    result = get_forecast(coords["lat"], coords["lng"])

    if not result:
        return jsonify({"error": "No se pudo obtener pronóstico"}), 500

    return jsonify({
        "ciudad": ciudad,
        "lat": coords["lat"],
        "lng": coords["lng"],
        "forecast": result
    }), 200