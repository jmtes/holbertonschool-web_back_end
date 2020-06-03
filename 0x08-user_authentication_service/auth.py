#!/usr/bin/env python3
''' Define auth functions. '''

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> str:
    ''' Encrypt password with bcrypt. '''
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    ''' Generate unique ID. '''
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        ''' Initialize Auth instance. '''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        ''' Register and add user to database. '''
        try:
            self._db.find_user_by(email=email)
            raise ValueError('User {:s} already exists.'.format(email))
        except NoResultFound:
            registered_user = self._db.add_user(email,
                                                _hash_password(password))
            return registered_user

    def valid_login(self, email: str, password: str) -> bool:
        ''' Check if password matches. '''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
