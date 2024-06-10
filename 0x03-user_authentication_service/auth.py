#!/usr/bin/env python3
"""Module: Authentication measures
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Task 4: Hashes password
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
