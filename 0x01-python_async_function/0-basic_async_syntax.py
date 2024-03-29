#!/usr/bin/env python3

"""Bascs of Async IO"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """random delay coroutine"""
    await_time: float = uniform(0, max_delay)
    await asyncio.sleep(await_time)
    return await_time
