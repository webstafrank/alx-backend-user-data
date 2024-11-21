#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with a random salt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted hash of the password.
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    # Hash the password
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed

