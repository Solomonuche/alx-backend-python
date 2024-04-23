#!/usr/bin/env python3
"""
Async IO
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    an asynchronous coroutine that takes in an integer argument
    waits for a random delay between 0 and max_delay
    """

    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
