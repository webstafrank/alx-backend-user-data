#!/usr/bin/env python3
"""
Module for logging with PII redaction using RedactingFormatter.
"""

import logging
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscate specified fields in a log message by replacing
    them with a redaction string.
    """
    pattern = '|'.join(f'{field}=[^ {separator}]*' for field in fields)
    return re.sub(pattern, lambda m: f"{m.group(0).split('=')[0]}={redaction}", message)

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class for logging PII fields """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize RedactingFormatter with fields to be redacted.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format log record with PII fields redacted.
        """
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)

