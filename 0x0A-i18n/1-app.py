#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def root():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('1-index.html')


class Config(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


if __name__ == "__main__":
    app.run()
