#!/usr/bin/env python3
''' Run Flask app. '''

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    ''' Configure Babel for i18n. '''
    LANGUAGES = ['en', 'fr']


babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    ''' Serve index page. '''
    return render_template('0-index.html')


@babel.localeselector
def get_locale():
    ''' Get locale. '''
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
