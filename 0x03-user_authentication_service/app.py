#!/usr/bin/env python3
"""
Flask app for user registration
"""

from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()

@app.route("/users", methods=["POST"])
def users():
    """
    POST /users route to register a user.

    Form data:
        - email: User email
        - password: User password
    
    Returns:
        JSON response with a message about registration success or failure.
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

