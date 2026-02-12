import requests 
from flask import Flask, jsonify, request


app = Flask(__name__)

PRODUCT_SERVICE_URL = "http://product-service/products"
ORDER_SERVICE_URL = "http://order-service/orders"
USER_SERVICE_URL = "http://user-service/users"

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/products")
def products():
    try:
        resp = requests.get(PRODUCT_SERVICE_URL, timeout=2)
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({
            "error": "product-service unavailable",
            "details": str(e)
        }), 503

@app.route("/orders", methods=["GET", "POST"])
def orders():
    try:
        if request.method == "POST":
            resp = requests.post(
                ORDER_SERVICE_URL,
                json=request.json,
                timeout=2
            )
        else:
            resp = requests.get(ORDER_SERVICE_URL, timeout=2)

        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({
            "error": "order-service unavailable",
            "details": str(e)
        }), 503

@app.route("/users", methods=["GET", "POST"])
def users():
    try:
        if request.method == "POST":
            resp = requests.post(
                USER_SERVICE_URL,
                json=request.get_json(),
                timeout=2
            )
        else:
            resp = requests.get(USER_SERVICE_URL, timeout=2)

        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({
            "error": "user-service unavailable",
            "details": str(e)
        }), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
