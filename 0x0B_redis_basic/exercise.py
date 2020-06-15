#!/usr/bin/env python3
''' Define Cache class for use with Redis. '''

import redis
from typing import Union, Optional, Callable
from uuid import uuid4
from sys import byteorder


def count_calls(method: Callable) -> Callable:
    ''' Track number of calls to method. '''
    key = method.__qualname__

    def wrapper(self, *args, **kwargs):
        ''' Wrapper for function. '''
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    ''' Cache class for use with Redis. '''

    def __init__(self) -> None:
        ''' Initialize instance of Cache. '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Store data in Redis store. '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
                                                                    bytes,
                                                                    int,
                                                                    float]:
        ''' Get data from Redis store. '''
        data = self._redis.get(key)

        if fn:
            data = fn(data)

        return data

    def get_str(b: bytes) -> str:
        ''' Convert bytes to string. '''
        return b.decode('utf-8')

    def get_int(b: bytes) -> str:
        ''' Convert bytes to integer. '''
        return int.from_bytes(b, byteorder)
