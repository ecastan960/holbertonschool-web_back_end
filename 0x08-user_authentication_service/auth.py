#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
from sqlalchemy.orm.exc import NoResultFound

from db import DB
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes str password
    """
    return bcrypt.hashpw(password.encode('utf-8'),
                         bcrypt.gensalt())
