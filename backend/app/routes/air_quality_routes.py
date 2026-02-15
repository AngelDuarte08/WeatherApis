from flask import Blueprint, request, jsonify
from app.services.air_quality_service import get_air_quality
from app.services.google_maps_service import get_coordinates

air_quality_bp = Blueprint("air_quality", __name__)

@air_quality_bp.route("/air-quality", methods=["POST"])
def air_quality():
    data = request.get_json()
    ciudad = data.get("ciudad")

    if not ciudad:
        return jsonify({"error": "Ciudad requerida"}), 400

    coords = get_coordinates(ciudad)

    if not coords:
        return jsonify({"error": "No se encontraron coordenadas"}), 404

    result = get_air_quality(coords["lat"], coords["lng"])

    if not result:
        return jsonify({"error": "No se pudo obtener calidad del aire"}), 500

    return jsonify({
        "ciudad": ciudad,
        "lat": coords["lat"],
        "lng": coords["lng"],
        "air_quality": result
    }), 200
