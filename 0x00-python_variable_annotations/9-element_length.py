#!/usr/bin/env python3
"""9. Let's duck type an iterable object
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """_summary_

    Args:
        lst (Iterable[Sequence]): list

    Returns:
        List[Tuple[Sequence, int]]: list
    """
    return [(i, len(i)) for i in lst]
