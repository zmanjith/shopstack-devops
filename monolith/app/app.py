from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/products")
def products():
    return jsonify(["Laptop", "Phone", "Tablet"])

@app.route("/orders")
def orders():
    return jsonify(["Order-1", "Order-2"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
