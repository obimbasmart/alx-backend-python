#!/usr/bin/env python3

"""execute multiple coroutines at the same time with async"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """execute multiple coroutines"""
    coroutines = [asyncio.create_task(
        wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(coroutines)]
