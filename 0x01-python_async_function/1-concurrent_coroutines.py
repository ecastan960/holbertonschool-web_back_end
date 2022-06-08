#!/usr/bin/env python3
"""_summary_
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int, optional): _description_. Defaults to 10.

    Returns:
        List[float]: _description_
    """
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return [j for j in sorted(delays)]
