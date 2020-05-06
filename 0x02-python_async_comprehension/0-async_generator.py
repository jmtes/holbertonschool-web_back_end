#!/usr/bin/env python3
''' Define async_generator coroutine. '''

from asyncio import sleep
from typing import Generator
from random import random


async def async_generator() -> Generator[float, None, None]:
    ''' Generator that yields a random value between 0 and 10 every second, 10
    times. '''
    for _i in range(10):
        await sleep(1)
        yield 10 * random()
