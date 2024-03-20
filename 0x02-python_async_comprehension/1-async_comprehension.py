#!/usr/bin/env python3

""" Async Comprehension"""

from random import random
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return a list of floats"""
    return [num async for num in async_generator()]
