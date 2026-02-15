from flask import Blueprint, request, jsonify
from app.services.google_maps_service import get_coordinates

location_bp = Blueprint("location", __name__)

@location_bp.route("/location", methods=["POST"])
def buscar_coordenadas():
    data = request.get_json()
    direccion = data.get("direccion")

    if not direccion:
        return jsonify({"error": "Direccion requerida"}), 400

    coords = get_coordinates(direccion)

    if not coords:
        return jsonify({"error": "No se pudo obtener coordenadas"}), 404

    return jsonify(coords), 200
