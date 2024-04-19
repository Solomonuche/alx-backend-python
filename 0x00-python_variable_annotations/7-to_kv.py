#!/usr/bin/env python3
"""python variable annotation"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes in a string and int/ float then return str and float tuple"""
    return (k, v ** 2)
