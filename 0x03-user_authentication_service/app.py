#!/usr/bin/env python3
"""
Basic Flask application
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """
    GET / route that returns a JSON payload.

    Returns:
        JSON response: {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

