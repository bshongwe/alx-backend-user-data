#!/usr/bin/env python3
"""Module: Authentication measures
"""
import bcrypt
from db import DB
from user import User

from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Task 4: Hashes password
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with auth DB.
    """

    def __init__(self):
        """Initializes a new Auth instance.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register new user into DB.

        Args:
            email (str): Email of user.
            password (str): Password of user.

        Returns:
            User: Newly created User object.

        Raises:
            ValueError: If a user already exists with
            provided email.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))
