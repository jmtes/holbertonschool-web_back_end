#!/usr/bin/env python3
''' Define filter_datum function. '''

import logging
import re
import mysql.connector
from typing import List
from os import getenv


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'ip')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    ''' Return `message` with personally identifiable information redacted. '''
    return re.sub(
        r'(\w+)=([\w\-./]+@*[\w\-./]+)', lambda x: x.group(1) + '=' + redaction
        if x.group(1) in fields else x.group(), message)


def get_logger() -> logging.Logger:
    ''' Set up and return logger object. '''
    log = logging.getLogger('user_data')
    log.setLevel(logging.INFO)
    log.propagate = False

    sh = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    sh.setFormatter(formatter)
    log.addHandler(sh)

    return log


def get_db():
    ''' Return connector to database. '''
    connector = mysql.connector.connect(
        user=getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=getenv('PERSONAL_DATA_DB_NAME'))

    return connector


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

    def __init__(self, fields: List[str]):
        ''' Initialize class instance. '''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        ''' Return formatted log record string with PII redacted. '''
        return filter_datum(
            self.fields,
            self.REDACTION,
            super(
                RedactingFormatter,
                self).format(record),
            self.SEPARATOR)
