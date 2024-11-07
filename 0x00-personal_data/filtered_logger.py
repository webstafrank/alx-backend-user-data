#!/usr/bin/env python3
"""
Module for filtering sensitive information in log messages.
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscate specified fields in a log message by replacing
    them with a redaction string.
    """
    pattern = '|'.join(f'{field}=[^ {separator}]*' for field in fields)
    return re.sub(pattern, lambda m: f"{m.group(0).split('=')[0]}={redaction}", message)

