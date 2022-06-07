#!/usr/bin/env python3
"""6. Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """type-annotated function

    Args:
        mxd_lst (List[Union[int, float]]): list of integers and floats

    Returns:
        float: sum of elements of mxd_lst as float
    """
    return sum(mxd_lst)
