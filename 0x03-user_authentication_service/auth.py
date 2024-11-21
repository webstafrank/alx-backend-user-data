#!/usr/bin/env python3
"""
Authentication module
"""
from db import DB
from user import User
from typing import Type
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with a random salt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted hash of the password.
    """
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> Type[User]:
        """
        Register a new user in the database.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            User: The created user object.

        Raises:
            ValueError: If a user with the email already exists.
        """
        try:
            # Check if the user already exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except Exception:
            # User not found, continue to register
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

