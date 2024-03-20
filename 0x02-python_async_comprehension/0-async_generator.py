#!/usr/bin/env python3

""" Async Generator"""

import asyncio
from typing import AsyncGenerator
from random import random


async def async_generator() -> AsyncGenerator[float, None]:
    """coroutine - yield a random number between"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random() * 10
