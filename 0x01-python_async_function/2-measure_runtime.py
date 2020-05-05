#!/usr/bin/env python3
''' Define measure_time function. '''

from time import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Return execution time for wait_n given `n` and `max_delay`. '''
    t0 = time()
    run(wait_n(n, max_delay))
    t1 = time()
    total_time = t1 - t0
    return total_time / n
