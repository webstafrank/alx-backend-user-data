#!/usr/bin/env python3
"""
Auth module for user authentication.
"""

import uuid
from db import DB


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def _generate_uuid(self) -> str:
        """
        Generate a new UUID string.

        Returns:
            str: A string representation of a new UUID.
        """
        return str(uuid.uuid4())

