#!/usr/bin/env python3

"""measure runtime"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure coroutine runtime"""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elaspsed_time = time.perf_counter() - start_time
    return elaspsed_time / n
