from flask import Blueprint

basic_bp = Blueprint("basic", __name__)


@basic_bp.route("/")
def home():
    """ Simulates the home page"""
    return {"status": "OK", "message": "Welcome to the API test"}


@basic_bp.route("/about")
def about():
    """Simulates the about page"""
    return {"status": "OK", "message": "API for testing purposes"}
