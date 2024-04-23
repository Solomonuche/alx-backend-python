#!/usr/bin/env python3
"""
Python - Async Comprehension
"""
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    """
    Async Comprehensions
    """
    return [i async for i in async_generator()]
