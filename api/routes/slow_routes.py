import time
import random
from flask import Blueprint

slow_bp = Blueprint("slow", __name__)


@slow_bp.route("/slow")
def slow_response():
    """ Simulate a slow API responce between 1s and 4s"""
    delay = random.uniform(1, 4)
    time.sleep(delay)
    return {"status": "OK", "delay_seconds": delay}
