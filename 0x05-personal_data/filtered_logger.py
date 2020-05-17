#!/usr/bin/env python3
''' Define filter_datum function. '''

from typing import List
from re import sub


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    ''' Return `message` with personally identifiable information redacted. '''
    regex = r'(\w+)=([\w\-.]+@*[\w\-.]+)'
    return sub(regex, lambda x: x.group(1) + '=' + redaction
               if x.group(1) in fields else x.group(), message)
