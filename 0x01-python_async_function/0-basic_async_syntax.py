#!/usr/bin/env python3
"""_summary_
"""
import random
import asyncio


async def wait_random(max_delay: int=10) -> float:
    """_summary_

    Args:
        max_delay (int, optional): _description_. Defaults to 10.

    Returns:
        float: _description_
    """
    t = random.uniform(0, max_delay)
    await asyncio.sleep(t)
    return t
