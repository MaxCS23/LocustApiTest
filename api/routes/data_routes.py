import json
import os
from flask import Blueprint, request, jsonify

data_bp = Blueprint("data", __name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data",
                         "sample_data.json")


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
    return jsonify(read_data())


@data_bp.route("/items", methods=["POST"])
def add_items():
    """POST request to add items"""
    data = read_data()
    new_item = request.json
    data.append(new_item)
    write_data(data=data)
    return jsonify(new_item), 201


@data_bp.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    """PUT request to update item"""
    data = read_data()
    if 0 <= item_id < len(data):
        data[item_id] = request.json
        write_data(data)
        return jsonify(data[item_id])
    return {"error": "Item not found"}, 404


@data_bp.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    """DELETE request to remove item"""
    data = read_data()
    if 0 <= item_id < len(data):
        remove = data.pop(item_id)
        write_data(data)
        return jsonify(remove)
    return {"error": "Item not found"}, 404
