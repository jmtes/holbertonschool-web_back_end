#!/usr/bin/env python3
''' Define wait_n function. '''

from typing import List
from bisect import bisect_right

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' Execute wait_random(max_delay) n times and return sorted list of delay
    times. '''
    delays = []
    for _i in range(n):
        delay = await wait_random(max_delay)
        idx = bisect_right(delays, delay)
        delays.insert(idx, delay)
    return delays
