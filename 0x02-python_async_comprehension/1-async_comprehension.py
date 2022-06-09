#!/usr/bin/env python3
"""_summary_

Yields:
    _type_: _description_
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """_summary_

    Returns:
        List[float]: _description_

    Yields:
        Iterator[List[float]]: _description_
    """
    return [n async for n in async_generator()]
