#!/usr/bin/python3
"""Techniques for API Security and Authentication"""
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)


"""Initializing"""
app = Flask(__name__)
auth = HTTPBasicAuth()

"""Dictionnary structure used to store users
data in memory with hashed password"""
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


"""Public route for 'Welcome' endpoint """


@app.route("/", methods=["GET"])
def home():
    """function returning welcome message"""
    return "Welcome to the Flask API!"


@auth.verify_password
def verify_password(username, password):
    """HTTPBasicAuth instance to first protect routes"""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


"""Protected route with basic authentification"""


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


"""Set secret key and seting up JWT in flask """
app.config["JWT_SECRET_KEY"] = "secret_key"
jwt = JWTManager(app)


"""Public route with the user login"""


@app.route("/login", methods=["POST"])
def login():
    """defines the token creating process with a provided payload"""
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        return jsonify({"message": "wrong password or username"}), 400

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"error": "wrong password or username"}), 401


"""Protected route requiring valid JWT token """


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()

    if current_user not in users:
        return jsonify({"error": "User not found"}), 404

    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    else:
        return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
