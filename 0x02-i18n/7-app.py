#!/usr/bin/env python3
"""
Flask app with timezone selection
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _
import pytz


class Config:
    """Configuration class for the Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Get user from request."""
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """Set user before each request."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Get the locale from the request."""
    # Check URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    
    # Check user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    
    # Check request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Get the timezone from the request."""
    # Check URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    
    # Check user settings
    if g.user and g.user.get('timezone'):
        try:
            return pytz.timezone(g.user.get('timezone'))
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    
    # Default to UTC
    return pytz.UTC


@app.route('/')
def index():
    """Render the index page."""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(debug=True) 