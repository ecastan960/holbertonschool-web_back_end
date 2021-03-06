#!/usr/bin/env python3
""" Module of Session views
"""
from os import getenv
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """_summary_

    Returns:
        _type_: _description_
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session = auth.create_session(users[0].id)
    SESSION_NAME = getenv("SESSION_NAME")
    return jsonify(user.to_json()).set_cookie(SESSION_NAME, session)


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """_summary_

    Returns:
        _type_: _description_
    """
    from api.v1.app import auth
    delete = auth.destroy_session(request)
    if not delete:
        abort(404)
    return jsonify({}), 200
