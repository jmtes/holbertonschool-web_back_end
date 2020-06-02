#!/usr/bin/env python3
''' Define auth functions. '''

import bcrypt


def _hash_password(password: str) -> str:
    ''' Encrypt password with bcrypt. '''
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
