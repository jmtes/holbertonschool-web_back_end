#!/usr/bin/env python3
''' Define BasicAuth class. '''

from api.v1.auth.auth import Auth
from models.user import User
from base64 import b64decode
from typing import TypeVar
import binascii


class BasicAuth(Auth):
    ''' Extend behaviors of Auth controller.

        Methods:
            extract_base_64_authorization_header - Return value of
            authorization header
            decode_base64_authorization_header - Return decoded value of
            Base64-encoded authorization header
            extract_user_credentials - Return a user's email and password
            user_object_from_credentials - Return User instance based on email
            and password
            current_user - Retrieve User instance for request
    '''

    def extract_base64_authorization_header(self, authorization_header: str) \
            -> str:
        ''' Return authorization header if valid. '''
        if authorization_header is None or not isinstance(authorization_header,
                                                          str):
            return None
        return authorization_header[6:] \
            if authorization_header.startswith('Basic ') else None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        ''' Return decoded value of Base64-encoded authorization header. '''
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            # Convert string to bytes
            header = base64_authorization_header.encode('utf-8')
            # Decode base64-encoded bytes
            header = b64decode(header)
            # Convert bytes back to string
            header = header.decode('utf-8')
            return header
        except BaseException:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        ''' Return user email and password based on authorization header
            value. '''
        if decoded_base64_authorization_header is None \
                or not isinstance(decoded_base64_authorization_header, str) \
                or ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> \
            TypeVar('User'):
        ''' Return User instance based on email and password.

            Return None if no user is found with the specified email OR if
            password is not valid. '''
        if user_email is None or user_pwd is None or not isinstance(
                user_email, str) or not isinstance(user_pwd, str):
            return None

        matching_users = User.search({'email': user_email})

        for user in matching_users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' Retrieve User instance for request.

            Return None on failure to retrieve user. '''

        # Get value of authorization header if there is one.
        auth_header_val = self.authorization_header(request)
        if not auth_header_val:
            return None

        # Extract value of authorization header and decode it.
        auth_header_val = self.extract_base64_authorization_header(
            auth_header_val)
        auth_header_val = self.decode_base64_authorization_header(
            auth_header_val)
        if not auth_header_val:
            return None

        # Extract user credentials from decoded authorization header.
        user_credentials = self.extract_user_credentials(auth_header_val)

        # Return User instance if email and password match
        return self.user_object_from_credentials(user_credentials[0],
                                                 user_credentials[1])
