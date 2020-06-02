#!/usr/bin/env python3
''' Set up and run Flask app. '''

from flask import Flask, jsonify
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    ''' GET /

        Return: Message '''
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    ''' POST /users

        Register a new user.

        JSON Body:
            email - user email
            password - user password

        Return: User email '''
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
