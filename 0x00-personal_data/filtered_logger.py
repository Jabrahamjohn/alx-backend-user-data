#!/usr/bin/env python3
"""filtered_logger module"""

import logging, re
from typing import List

def filter_datum(fields: str, redaction: str, message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        message = re.sub(rf'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message