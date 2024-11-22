from flask import Flask, request, jsonify, redirect, abort
from auth import Auth

app = Flask(__name__)

AUTH = Auth()

@app.route("/sessions", methods=["DELETE"])
def logout():
    """
    Logs the user out by destroying their session.
    The session ID is expected as a cookie.
    """
    # Get the session_id from cookies
    session_id = request.cookies.get("session_id")

    # Check if the session_id exists and is valid
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        # Destroy the session by setting session_id to None
        AUTH.destroy_session(user.id)
        return redirect("/")  # Redirect to the home route
    else:
        # If no user is found, return a 403 error
        abort(403, "Unauthorized access: Invalid session ID")

