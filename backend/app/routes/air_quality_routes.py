from flask import Blueprint, request, jsonify
from app.services.air_quality_service import get_air_quality

air_quality_bp = Blueprint("air_quality", __name__)

@air_quality_bp.route("/air-quality", methods=["GET"])
def air_quality():
    lat = request.args.get("lat")
    lng = request.args.get("lng")

    if not lat or not lng:
        return jsonify({"error": "lat y lng requeridos"}), 400

    result = get_air_quality(float(lat), float(lng))

    if not result:
        return jsonify({"error": "No se pudo obtener calidad del aire"}), 500

    return jsonify(result), 200
