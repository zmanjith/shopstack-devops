from flask import Flask, jsonify, request
import requests
import json
import os

app = Flask(__name__)

PRODUCT_SERVICE_URL = "http://product-service/products"
DATA_FILE = "/data/orders.json"

os.makedirs("/data", exist_ok=True)

def load_orders():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_orders(orders):
    with open(DATA_FILE, "w") as f:
        json.dump(orders, f)

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/orders", methods=["GET", "POST"])
def orders():
    orders = load_orders()

    if request.method == "POST":
        data = request.get_json()
        if not data or "product_id" not in data:
            return jsonify({"error": "product_id required"}), 400

        product_id = data["product_id"]

        try:
            resp = requests.get(PRODUCT_SERVICE_URL, timeout=2)
            products = resp.json()
        except Exception as e:
            return jsonify({"error": "product-service unavailable"}), 503

        if not any(p["id"] == product_id for p in products):
            return jsonify({"error": "Invalid product"}), 400

        order = {
            "id": len(orders) + 1,
            "product_id": product_id
        }
        orders.append(order)
        save_orders(orders)

    return jsonify(orders)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

