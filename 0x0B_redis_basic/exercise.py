#!/usr/bin/env python3
"""Redis exercise task 0
"""
import redis
import uuid
from typing import Optional, Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """_summary_

    Args:
        method (Callable): _description_

    Returns:
        Callable: _description_
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """_summary_

    Args:
        method (Callable): _description_

    Returns:
        Callable: _description_
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


class Cache:
    """_summary_
    """

    def __init__(self):
        """_summary_
        """
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    @call_history
    @count_calls
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

    def get(self, key: str,
            fn: Optional[Callable]) -> Union[str, bytes, int]:
        """_summary_

        Args:
            key (str): _description_
            fn (Optional[Callable]): _description_

        Returns:
            Union[str, bytes, int]: _description_
        """
        data = self.__redis.get(key)
        if fn:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> str:
        """_summary_

        Args:
            key (str): _description_

        Returns:
            str: _description_
        """
        return self.__redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """_summary_

        Args:
            key (str): _description_

        Returns:
            int: _description_
        """
        data = self.__redis.get(key)
        try:
            data = int(data.decode("utf-8"))
        except:
            data = 0
        return data
