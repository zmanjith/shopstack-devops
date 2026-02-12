from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/products")
def products():
    return jsonify([
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Phone"},
        {"id": 3, "name": "Tablet"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
