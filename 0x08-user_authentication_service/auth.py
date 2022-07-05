#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
from sqlalchemy.orm.exc import NoResultFound

from db import DB
import bcrypt
from user import User


def _hash_password(password: str) -> bytes:
    """_summary_

    Args:
        password (str): _description_

    Returns:
        bytes: _description_
    """
    return bcrypt.hashpw(password.encode('utf-8'),
                         bcrypt.gensalt())


class Auth:
    """_summary_
    """

    def __init__(self):
        """_summary_
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """_summary_

        Args:
            email (str): _description_
            password (str): _description_

        Raises:
            ValueError: _description_

        Returns:
            User: _description_
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(
                "User {} already exists".format(email))
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
