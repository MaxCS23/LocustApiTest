import json
import os
import threading
from flask import Blueprint, request, jsonify

data_bp = Blueprint("data", __name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data",
                         "sample_data.json")

file_lock = threading.Lock()


def read_data():
    """Returns the data from the JSON file"""
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def write_data(data):
    """ Writes data to the JSON file"""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


@data_bp.route("/items", methods=["GET"])
def get_items():
    """GET request including the items"""
    with file_lock:
        return jsonify(read_data())


@data_bp.route("/items", methods=["POST"])
def add_items():
    """POST request to add items"""
    with file_lock:
        data = read_data()
        new_item = request.json
        if not new_item:
            return {"error": "Invalid or missing JSON data"}, 400

        max_id = max([item["id"] for item in data], default=0)
        new_item["id"] = max_id + 1

        data.append(new_item)
        write_data(data)
        return jsonify(new_item), 201


@data_bp.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    """PUT request to update item"""
    with file_lock:
        data = read_data()
        updates = request.json

        for item in data:
            if item["id"] == item_id:
                item.update(updates)
                write_data(data)
                return jsonify(item), 200

        return {"error": "Item not found"}, 404


@data_bp.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    """DELETE request to remove item"""
    with file_lock:
        data = read_data()

        for i, item in enumerate(data):
            if item["id"] == item_id:
                deleted_item = data.pop(i)
                write_data(data)
                return jsonify(deleted_item), 200
        return {"error": "Item not found"}, 404
