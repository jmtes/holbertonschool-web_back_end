#!/usr/bin/env python3
''' Define BasicAuth class. '''

from api.v1.auth.auth import Auth
from base64 import b64decode
import binascii


class BasicAuth(Auth):
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
        except binascii.Error:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        ''' Return user email and password. '''
        if decoded_base64_authorization_header is None \
                or not isinstance(decoded_base64_authorization_header, str) \
                or ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':'))
