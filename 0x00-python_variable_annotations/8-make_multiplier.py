#!/usr/bin/env python3
"""8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated

    Args:
        multiplier (float): number to multiply

    Returns:
        Callable[[float], float]: function float * multiplier
    """
    return lambda n: n * multiplier
