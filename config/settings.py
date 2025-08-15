import os

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000/")
MIN_WAIT = os.getenv("MIN_WAIT", 1)
MAX_WAIT = os.getenv("MAX_WAIT", 5)
