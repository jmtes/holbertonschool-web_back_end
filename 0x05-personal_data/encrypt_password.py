#!/usr/bin/env python3
''' Define hash_password function. '''

import bcrypt


def hash_password(password: str) -> bytes:
    ''' Return encrypted password. '''
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    ''' Check whether or not password matches hashed password. '''
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    return False
