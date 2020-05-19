#!/usr/bin/env python3
''' Define Auth class. '''

from flask import request
from typing import List, TypeVar


class Auth:
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

        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
