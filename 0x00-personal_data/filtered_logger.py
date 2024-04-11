#!/usr/bin/env python3
"""filtered_logger module"""

import logging, re
from typing import List

def filter_datum(fields: str, redaction: str, message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        """replaces the field with the redaction"""
        message = re.sub(rf'{field}=.*?{separator}',
                         """
                         args:
                         fields: {fields}
                         redaction: {redaction}
                         message: {message}
                         separator: {separator}
                         """
                         f'{field}={redaction}{separator}', message)
    return message

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError