#!/usr/bin/env python3
"""
Flask app for authentication.
"""

from flask import Flask, request, jsonify, abort, make_response
from auth import Auth

app = Flask(__name__)
AUTH = Auth()

@app.route("/sessions", methods=["POST"])
def login():
    """
    POST /sessions route for user login.

    Returns:
        Response object:
            - JSON payload with success message if login succeeds.
            - 401 status code if login fails.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not AUTH.valid_login(email, password):
        abort(401)  # Unauthorized

    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

