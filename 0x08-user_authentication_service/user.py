#!/usr/bin/env python3
"""_summary_
"""
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """_summary_

    Returns:
        _type_: _description_
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=False)
