#!/usr/bin/env python3
''' Define filter_datum function. '''

import logging
import re
import mysql.connector
from typing import List
import os


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


def get_db() -> mysql.connector.connection.MySQLConnection:
    ''' Return connector to database. '''
    connector = mysql.connector.connect(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME'))

    return connector


def main() -> None:
    ''' Log user info from database. '''
    db = get_db()
    cursor = db.cursor()

    query = ('SELECT * FROM users')
    cursor.execute(query)

    format_1 = 'name={:s}; email={:s}; phone={:s}; ssn={:s}; password={:s}; '
    format_2 = 'ip={:s}; last_login={}; user_agent={:s};'
    format_str = format_1 + format_2
    for (name, email, phone, ssn, password, ip, last_login, user_agent) \
            in cursor:
        print(format_str.format(name, email, phone, ssn, password, ip,
                                last_login, user_agent))

    cursor.close()
    db.close()


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


if __name__ == '__main__':
    main()
