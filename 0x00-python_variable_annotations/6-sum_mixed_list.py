#!/usr/bin/env python3
''' Define sum_mixed_list function.

    Attributes:
      sum_mixed_list - function that returns sum of elements of list
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Return sum of elements of mxd_list. '''
    return sum(mxd_lst)
