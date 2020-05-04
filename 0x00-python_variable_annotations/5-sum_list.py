#!/usr/bin/env python3
''' Define sum_list function.

    Attributes:
      sum_list - function that returns sum of all elements of a list
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Return sum of all elements in input_list. '''
    return sum(input_list)
