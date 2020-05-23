#!/usr/bin/env python3
''' Define SessionAuth class. '''

from api.v1.auth.auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    ''' Extend behavior of Auth class for session authentication. '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        ''' Create and return a session ID for a user ID. '''
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        ''' Return user ID associated with specified session ID. '''
        if session_id is None or not isinstance(session_id, str):
            return None

        return SessionAuth.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        ''' Return User instance based on request cookie value. '''
        # Get session ID from request cookie
        session_id = self.session_cookie(request)

        # Get user ID associated with session ID
        user_id = self.user_id_for_session_id(session_id)

        return User.get(user_id)

    def destroy_session(self, request=None):
        ''' Destroy session associated with request. '''
        # Get session ID from request cookie
        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        # Get user ID associated with session ID
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        # Remove session ID from dict
        del SessionAuth.user_id_by_session_id[session_id]
        return True
