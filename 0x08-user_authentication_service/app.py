#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
from flask import Flask, jsonify, abort, redirect
from auth import Auth
from flask.globals import request
from flask.helpers import make_response

AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def greetings():
    """_summary_

    Returns:
        _type_: _description_
    """
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """_summary_

    Returns:
        _type_: _description_
    """
    try:
        email = request.form['email']
        password = request.form['password']
        user = AUTH.register_user(email, password)
        if user:
            return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """_summary_

    Returns:
        _type_: _description_
    """
    email = request.form['email']
    password = request.form['password']
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        result = make_response(jsonify({"email": email,
                                        "message": "logged in"}))
        result.set_cookie('session_id', session_id)
        return result
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """_summary_

    Returns:
        _type_: _description_
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None or session_id is None:
        abort(403)
    else:
        AUTH.destroy_session(user.id)
        return redirect("/")


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """_summary_

    Returns:
        _type_: _description_
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None or session_id is None:
        abort(403)
    else:
        return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """_summary_

    Returns:
        _type_: _description_
    """
    email = request.form['email']
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """_summary_

    Returns:
        _type_: _description_
    """
    email = request.form['email']
    reset_token = request.form['reset_token']
    new_password = request.form['new_password']
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({
            "email": email,
            "message": "Password updated"}), 200
    except Exception:
        abort(403)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
