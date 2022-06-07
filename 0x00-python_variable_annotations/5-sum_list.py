#!/usr/bin/env python3
"""5. Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """type-annotated function

    Args:
        input_list (List[float]): List of float numbers

    Returns:
        float: sum of elements of input list
    """
    return sum(input_list)
