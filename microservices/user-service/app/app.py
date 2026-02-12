from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

DATA_FILE = "/data/users.json"
os.makedirs("/data", exist_ok=True)

def load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f)

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/users", methods=["GET", "POST"])
def users():
    users = load_users()

    if request.method == "POST":
        data = request.get_json()
        if not data or "name" not in data:
            return jsonify({"error": "name required"}), 400

        user = {
            "id": len(users) + 1,
            "name": data["name"]
        }
        users.append(user)
        save_users(users)

    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
