#!/usr/bin/env python3
"""
Module for securely connecting to a database and logging user information with PII redaction.
"""

import os
import mysql.connector
import logging
from typing import List, Tuple
from mysql.connector.connection import MySQLConnection

PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscate specified fields in a log message by replacing
    them with a redaction string.
    """
    import re
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

def get_logger() -> logging.Logger:
    """
    Returns a logger named "user_data" configured with a StreamHandler and
    RedactingFormatter to redact sensitive PII fields.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)

    return logger

def get_db() -> MySQLConnection:
    """
    Connect to a MySQL database using credentials from environment variables.
    Returns:
        MySQLConnection: a connection object to the database
    """
    user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    if not database:
        raise ValueError("Database name not provided. Set PERSONAL_DATA_DB_NAME.")

    return mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )

def main() -> None:
    """
    Main function to connect to the database, retrieve all users, and log each user record
    with sensitive PII fields redacted.
    """
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()

    # Query to retrieve all records from the users table
    cursor.execute("SELECT name, email, phone, ssn, password, ip, last_login, user_agent FROM users;")
    
    # Fetch and log each row with PII redaction
    for row in cursor.fetchall():
        # Format the row into a log-friendly string
        message = ("name={}; email={}; phone={}; ssn={}; password={}; "
                   "ip={}; last_login={}; user_agent={}").format(*row)
        logger.info(message)
    
    # Clean up database resources
    cursor.close()
    db.close()

# Only run the main function if the module is executed directly
if __name__ == "__main__":
    main()

