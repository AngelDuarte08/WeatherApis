from flask import Flask
from app.routes.weather_routes import weather_bp
from app.routes.location_routes import location_bp
from app.routes.air_quality_routes import air_quality_bp
from app.routes.twilio_routes import twilio_bp


def create_app():
    app = Flask(__name__)

    # Registrar Blueprints
    app.register_blueprint(weather_bp, url_prefix="/api")
    app.register_blueprint(location_bp, url_prefix="/api")
    app.register_blueprint(air_quality_bp, url_prefix="/api")
    app.register_blueprint(twilio_bp, url_prefix="/api/twilio")

    return app
