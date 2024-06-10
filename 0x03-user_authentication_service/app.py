#!/usr/bin/env python3
"""Basic Flask app with user auth features.
"""
from flask import Flask, jsonify, request, abort, redirect

from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """GET /
    Route handler for root endpoint.

    Return:
        - Home page's payload.
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """POST /users
    Endpoint to register a user.

    Return:
        - The account creation payload.
    """
    email, password = request.form.get("email"), request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """POST /sessions
    Login endpoint to create a new session.

    Return:
        - The account login payload.
    """
    email, password = request.form.get("email"), request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response

def destroy_session(self, user_id: int) -> None:
        """Destroy user's session by setting their
        session ID to None.

        Args:
            user_id (int): The ID of the user.
        """
        if user_id is None:
            return None
        self._db.update_user(user_id, session_id=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
