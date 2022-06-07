#!/usr/bin/env python3
"""7. Complex types - string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """type-annotated function

    Args:
        k (str): string
        v (Union[int, float]): int or float number

    Returns:
        Tuple[str, float]: tuple with string and square of v
    """
    return (k, v ** 2)
