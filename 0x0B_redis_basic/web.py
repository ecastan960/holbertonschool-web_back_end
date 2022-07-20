#!/usr/bin/env python3
"""_summary_
"""

import redis
from typing import Callable
from functools import wraps
from requests import get


def count_requests(method: Callable) -> Callable:
    """_summary_

    Args:
        method (Callable): _description_

    Returns:
        Callable: _description_
    """
    @wraps(method)
    def wrapper(url):
        """_summary_

        Args:
            url (_type_): _description_

        Returns:
            _type_: _description_
        """
        redis.Redis().incr(f"count:{url}")
        cache = redis.Redis().get(f"cached:{url}")
        if cache:
            return cache.decode('utf-8')
        html = method(url)
        redis.Redis().setex(f"cached:{url}", 10, html)
        return html
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """_summary_

    Args:
        url (str): _description_

    Returns:
        str: _description_
    """
    response = get(url)
    return response.text
