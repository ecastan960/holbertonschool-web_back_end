#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension(),
                           async_comprehension(),
                           async_comprehension(),
                           async_comprehension()))
    runtime = time.perf_counter() - start
    return runtime
