#!/usr/bin/env python3
"""_summary_

Returns:
_type_: _description_
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """_summary_

    Args:
        password (str): _description_

    Returns:
        bytes: _description_
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
