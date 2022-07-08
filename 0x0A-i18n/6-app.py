#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


@babel.localeselector
def get_locale():
    """_summary_

    Returns:
        _type_: _description_
    """
    lang = request.args.get('locale')
    configLang = app.config['LANGUAGES']
    if lang in configLang:
        return lang
    userId = request.args.get('login_as')
    if userId:
        lang = users[int(userId)]['locale']
        if lang in configLang:
            return lang
    lang = request.headers.get('locale')
    if lang in configLang:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """_summary_

    Returns:
        _type_: _description_
    """
    try:
        userId = request.args.get('login_as')
        return users[int(userId)]
    except Exception:
        return None


@app.before_request
def before_request():
    """_summary_
    """
    g.user = get_user()


if __name__ == "__main__":
    app.run()
