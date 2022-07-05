#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
from sqlalchemy.orm.exc import NoResultFound

from db import DB
import bcrypt


def _hash_password(password: str) -> bytes:
    """_summary_

    Args:
        password (str): _description_

    Returns:
        bytes: _description_
    """
    return bcrypt.hashpw(password.encode('utf-8'),
                         bcrypt.gensalt())
