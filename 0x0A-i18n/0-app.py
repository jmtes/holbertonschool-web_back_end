#!/usr/bin/env python3
''' Run Flask app. '''

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    LANGUAGES = ['en', 'fr']


babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    ''' Serve index page. '''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
