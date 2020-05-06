#!/usr/bin/env python3
''' Define measure_runtime function. '''

from time import time
from asyncio import gather

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Measure the runtime of async_comprehension executed 4 times in
    parallel. '''
    t0 = time()
    await gather(async_comprehension(),
                 async_comprehension(),
                 async_comprehension(),
                 async_comprehension())
    t1 = time()

    return t1 - t0
