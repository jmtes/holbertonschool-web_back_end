#!/usr/bin/env python3
''' Define auth session routes. '''

from api.v1.views import app_views
from models.user import User
from flask import request, jsonify, abort
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login() -> str:
    ''' Log user in. '''

    # Get user email and password
    user_email = request.form.get('email', None)
    user_pwd = request.form.get('password', None)

    if user_email is None:
        return jsonify({'error': 'email missing'}), 400
    if user_pwd is None:
        return jsonify({'error': 'password missing'}), 400

    # Look for users with specified email
    found_user = User.search({'email': user_email})

    if not found_user:
        return jsonify({'error': 'no user found for this email'}), 404

    found_user = found_user[0]

    # Validate password
    if not found_user.is_valid_password(user_pwd):
        return jsonify({'error': 'wrong password'}), 401

    # Import auth
    from api.v1.app import auth

    # Create session ID for user
    session_id = auth.create_session(found_user.id)

    # Set response cookie
    cookie_name = getenv('SESSION_NAME')

    res = jsonify(found_user.to_json())
    res.set_cookie(cookie_name, session_id)

    return res


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def auth_session_logout() -> str:
    ''' Destroy session and log user out. '''
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
