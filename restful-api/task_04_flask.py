#!/usr/bin/python3
"""flask API"""

from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_json_data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def user_profile(username):
    profile = users.get(username)
    
    if not profile:
        return jsonify({"error": "User not found"}), 404
    else:
        return jsonify(profile)

@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    username = user_data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 404
    else:
        user_data = {
            "username": username,
            "name": user_data.get("name"),
            "age": user_data.get("age"),
            "city": user_data.get("city"),
        }

    users[username] = user_data

    return jsonify({"message": "User added", "User": user_data}),201

if __name__ == "__main__":
    app.run()