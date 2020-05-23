#!/usr/bin/env python3
''' Define Auth class. '''

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    ''' Auth Controller

        Methods:
          require_auth - Check if path requires authentication
          authorization_header - Check if request is authorized
          current_user - Return current user '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' Determine whether or not path requires authentication.

            Arguments:
              path - the path to check
              excluded_paths - list of paths that do not require authentication

            Return: True if path requires authentication, False otherwise '''
        if path is None or excluded_paths is None:
            return True

        if path[-1] != '/':
            path += '/'

        wildcard_paths = [p[:-1] for p in excluded_paths if p[-1] == '*']

        for p in wildcard_paths:
            if path.startswith(p):
                return False

        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        ''' Return value of Authorization header if request is authorized,
        False otherwise. '''
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        ''' Return current user. '''
        return None

    def session_cookie(self, request=None):
        ''' Return cookie value from request. '''
        if request is None:
            return None

        cookie_key = getenv('SESSION_NAME')

        return request.cookies.get(cookie_key, None)
