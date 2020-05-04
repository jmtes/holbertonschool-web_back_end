#!/usr/bin/env python3
'''
  Attributes:
    T - a TypeVar with value '~T'
    safely_get_value - function that returns value of a specified key in a dict
'''

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    ''' Return dct[key] if it exists, otherwise return `default`. '''
    if key in dct:
        return dct[key]
    else:
        return default
