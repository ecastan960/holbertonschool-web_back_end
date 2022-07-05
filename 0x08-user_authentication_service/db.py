#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """_summary_

        Args:
            email (str): _description_
            hashed_password (str): _description_

        Returns:
            User: _description_
        """
        DBSession = self._session
        new_user = User(email=email, hashed_password=hashed_password)
        DBSession.add(new_user)
        DBSession.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """_summary_

        Raises:
            NoResultFound: _description_

        Returns:
            User: _description_
        """
        DBSession = self._session
        query = DBSession.query(User).filter_by(**kwargs)
        user = query.first()
        if (user is None):
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """_summary_

        Args:
            user_id (int): _description_

        Raises:
            ValueError: _description_
        """
        DBSession = self._session
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if hasattr(user, key) is False:
                raise ValueError
            setattr(user, key, value)
        DBSession.commit()
