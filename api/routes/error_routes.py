from flask import Blueprint

error_bp = Blueprint("error", __name__)


@error_bp.route("/error500")
def error_500():
    """Simulates an internal server error '500'"""
    return {"error": "Internal Server Error"}, 500


@error_bp.route("/error404")
def error_404():
    """Simulates a Resource not found error '404'"""
    return {"error": "Resource not found"}, 404
