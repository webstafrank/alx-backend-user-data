#!/usr/bin/env python3
"""
Module for connecting to a secure MySQL database using environment variables.
"""

import os
import mysql.connector
from mysql.connector.connection import MySQLConnection
from typing import Optional

def get_db() -> MySQLConnection:
    """
    Connect to a MySQL database using credentials from environment variables.
    Returns:
        MySQLConnection: a connection object to the database
    """
    # Retrieve database credentials from environment variables
    user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    # Ensure that the database name is provided
    if not database:
        raise ValueError("Database name not provided. Set PERSONAL_DATA_DB_NAME.")

    # Establish and return the database connection
    return mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )

