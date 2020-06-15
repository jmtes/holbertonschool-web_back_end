#!/usr/bin/env python3
''' Define Cache class for use with Redis. '''

import redis
from typing import Union, Optional, Callable
from uuid import uuid4
from sys import byteorder
from functools import wraps


def count_calls(method: Callable) -> Callable:
    ''' Track number of calls to method. '''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' Wrapper for function. '''
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    ''' Track history of inputs to and outputs of a function. '''
    in_key = method.__qualname__ + ':inputs'
    out_key = method.__qualname__ + ':outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' Wrapper for function. '''
        self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(out_key, str(output))
        return output

    return wrapper


class Cache:
    ''' Cache class for use with Redis. '''

    def __init__(self) -> None:
        ''' Initialize instance of Cache. '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
