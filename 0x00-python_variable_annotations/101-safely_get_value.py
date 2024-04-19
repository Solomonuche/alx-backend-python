#!/usr/bin/env python3
"""
Python - Variable Annotations module
"""
from typing import Any, Union, TypeVar, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    any type annotation function
    """
    if lst:
        return lst[0]
    else:
        return None
