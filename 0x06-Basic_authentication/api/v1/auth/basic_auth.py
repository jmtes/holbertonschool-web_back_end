#!/usr/bin/env python3
''' Define BasicAuth class. '''

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    def extract_base64_authorization_header(self, authorization_header: str) \
            -> str:
        ''' Return authorization header if valid. '''
        if authorization_header is None or not isinstance(authorization_header,
                                                          str):
            return None
        return authorization_header[6:] \
            if authorization_header.startswith('Basic ') else None
