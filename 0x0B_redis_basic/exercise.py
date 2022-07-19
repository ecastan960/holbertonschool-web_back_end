#!/usr/bin/env python3
"""Redis exercise task 0
"""
import redis
import uuid
from typing import Optional, Callable, Union


class Cache:
    """_summary_
    """

    def __init__(self) -> None:
        """_summary_
        """
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """_summary_

        Args:
            data (_type_): _description_

        Returns:
            str: _description_
        """
        key = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key
