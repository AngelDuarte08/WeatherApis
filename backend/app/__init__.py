from flask import Flask
from app.routes.location_routes import location_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(location_bp, url_prefix="/api")

    return app
