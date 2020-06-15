#!/usr/bin/env python3
''' Define Cache class for use with Redis. '''

import redis
from typing import Union
from uuid import uuid4


class Cache:
    ''' Cache class for use with Redis. '''

    def __init__(self) -> None:
        ''' Initialize instance of Cache. '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Store data in Redis store. '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key
