#!/usr/bin/env python3
"""Module: Authentication measures
"""
import bcrypt
from db import DB
from user import User

from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """Task 4: Hashes password
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

def _generate_uuid() -> str:
    """Task 9: Generates a UUID.
    """
    return str(uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """Checks if a user's login details are valid.
        """
        user = None
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                return bcrypt.checkpw(
                    password.encode("utf-8"),
                    user.hashed_password,
                )
        except NoResultFound:
            return False
        return False
