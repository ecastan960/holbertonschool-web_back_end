#!/usr/bin/env python3
"""10. Duck typing - first element of a sequence
"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """_summary_

    Args:
        lst (Sequence[Any]): list

    Returns:
        Union[Any, None]: first element or none
    """
    if lst:
        return lst[0]
    else:
        return None
