#!/usr/bin/env python3
''' Define filter_datum function. '''

import logging
from typing import List
from re import sub


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    ''' Return `message` with personally identifiable information redacted. '''
    regex = r'(\w+)=([\w\-.]+@*[\w\-.]+)'
    return sub(regex, lambda x: x.group(1) + '=' + redaction
               if x.group(1) in fields else x.group(), message)


class RedactingFormatter(logging.Formatter):
    ''' Define behaviors for obfuscating PII.

        Attributes:
          REDACTION - string to replace fields containing PII with
          FORMAT - outlines formatting that fields should have
          SEPARATOR - character(s) used to separate fields

        Methods:
          format - method filters values of incoming log records
    '''
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        ''' Initialize class instance. '''
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        ''' Filter values in log records. '''
        raise NotImplementedError
