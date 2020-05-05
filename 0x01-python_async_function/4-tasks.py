#!/usr/bin/env python3
''' Define task_wait_n function. '''

from typing import List
from bisect import bisect_right

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' Execute task_wait_random(max_delay) n times and return sorted list of delay
    times. '''
    delays = []
    for _i in range(n):
        delay = await task_wait_random(max_delay)
        idx = bisect_right(delays, delay)
        delays.insert(idx, delay)
    return delays
