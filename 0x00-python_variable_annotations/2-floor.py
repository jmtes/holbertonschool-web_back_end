#!/usr/bin/env python3
''' Define the floor function.

    Attributes:
      floor - function that calculates the floor of a float
'''


def floor(n: float) -> int:
    ''' Return largest int value less than or equal to n. '''
    return int(n) if n >= 0 else int(n) - 1
