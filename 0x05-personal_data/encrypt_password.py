#!/usr/bin/env python3
''' Define hash_password function. '''

import bcrypt


def hash_password(password: str) -> bytes:
    ''' Return encrypted password. '''
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
