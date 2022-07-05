#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
from flask import Flask, jsonify, abort
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
