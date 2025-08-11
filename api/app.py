from flask import Flask
from api.routes.basic_routes import basic_bp
from api.routes.data_routes import data_bp
from api.routes.error_routes import error_bp
from api.routes.slow_routes import slow_bp


def create_app() -> Flask:
    """Just create the flask app"""
    app = Flask(__name__)

    app.register_blueprint(basic_bp)
    app.register_blueprint(slow_bp)
    app.register_blueprint(error_bp)
    app.register_blueprint(data_bp)

    return app
