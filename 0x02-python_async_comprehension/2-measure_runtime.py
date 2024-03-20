#!/usr/bin/env python3

"""Run time for four parallel comprehensions mandatory
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure coroutine runtime"""
    start_time = time.perf_counter()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    asyncio.gather(*tasks, return_exceptions=True)
    elaspsed_time = time.perf_counter() - start_time
    return elaspsed_time
