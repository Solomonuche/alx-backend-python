#!/usr/bin/env python3
"""
Python - Variable Annotations module
"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    any type annotation function
    """
    if lst:
        return lst[0]
    else:
        return None
