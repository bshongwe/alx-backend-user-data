#!/usr/bin/env python3
"""Basic Flask app with user auth features.
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """GET /
    Route handler for root endpoint.

    Return:
        - Home page's payload.
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
