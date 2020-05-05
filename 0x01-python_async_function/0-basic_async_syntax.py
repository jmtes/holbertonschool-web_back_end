#!/usr/bin/env python3
''' Define wait_random function. '''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' Wait up to `max_delay` seconds and then return length of delay. '''
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
