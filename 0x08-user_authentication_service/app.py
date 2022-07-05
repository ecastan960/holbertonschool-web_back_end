#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
from flask import Flask, jsonify
from auth import Auth
from flask.globals import request

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
