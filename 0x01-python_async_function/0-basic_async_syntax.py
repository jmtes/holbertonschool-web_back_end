#!/usr/bin/env python3
''' Define wait_random function. '''

from asyncio import sleep
from random import random


async def wait_random(max_delay: int = 10) -> float:
    ''' Wait up to `max_delay` seconds and then return length of delay. '''
    delay = max_delay * random()
    await sleep(delay)
    return delay
