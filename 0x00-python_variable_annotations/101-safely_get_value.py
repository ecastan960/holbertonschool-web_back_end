#!/usr/bin/env python3
"""_summary_
"""
from typing import Union, Any, Mapping, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """_summary_

    Args:
        dct (Mapping): _description_
        key (Any): _description_
        default (Union[T, None], optional): _description_. Defaults to None.

    Returns:
        Union[Any, T]: _description_
    """    
    if key in dct:
        return dct[key]
    else:
        return default
