#!/usr/bin/env python3
"""filtered_logger module"""
import logging

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        filtered_values = map(self.filter_datum, [getattr(record, field, '') for field in self.fields])
        record.msg = self.SEPARATOR.join(filtered_values)
        return super().format(record)

    def filter_datum(self, message: str) -> str:
        return self.REDACTION
