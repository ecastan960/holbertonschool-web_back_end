#!/usr/bin/env python3
"""_summary_

Yields:
    _type_: _description_
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """_summary_

    Yields:
        Generator[float, None, None]: _description_
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
