#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
from flask import Flask, jsonify
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def message():
    """_summary_

    Returns:
        _type_: _description_
    """
    return jsonify({'message': 'Bienvenue'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
