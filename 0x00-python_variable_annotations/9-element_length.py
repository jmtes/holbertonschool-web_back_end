#!/usr/bin/env python3
''' Define element_length function.
'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Return list of tuples, one for each element, of which
    consists of the element itself and its length. '''
    return [(i, len(i)) for i in lst]
