#!/usr/bin/env python3
"""_summary_
"""
from datetime import timedelta
import datetime
from os import getenv
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from api.v1.auth.session_auth import SessionAuth
from models.user import User
from uuid import uuid4


class SessionExpAuth(SessionAuth):
    """_summary_

    Args:
        Auth (_type_): _description_

    Returns:
        _type_: _description_
    """

    def __init__(self):
        """_summary_
        """
        SESSION_DURATION = getenv('SESSION_DURATION')
        try:
            session_duration = int(SESSION_DURATION)
        except Exception:
            session_duration = 0
        self.session_duration = session_duration

    def create_session(self, user_id=None):
        """_summary_

        Args:
            user_id (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        session = super().create_session(user_id)
        if session is None:
            return None
        session_dict = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session] = session_dict
        return session

    def user_id_for_session_id(self, session_id=None):
        """_summary_

        Args:
            session_id (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id.keys():
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None
        if self.session_duration <= 0:
            return session_dict.get('user_id')
        created = session_dict.get('created_at')
        if created is None:
            return None
        time = created + timedelta(seconds=self.session_duration)
        if time < datetime.now():
            return None
        return session_dict.get('user_id')
