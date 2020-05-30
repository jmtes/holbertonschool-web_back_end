#!/usr/bin/env python3
''' Define DB class. '''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from user import Base, User


class DB:
    ''' DB class. '''
    def __init__(self):
        ''' Initialize DB instance. '''
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        ''' Create session if it does not exist and return it. '''
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        ''' Create user with given email/password and return new User instance.
        '''
        new_user = User(email=email, hashed_password=hashed_password)
        self.__session.add(new_user)
        self.__session.commit()
        return new_user
