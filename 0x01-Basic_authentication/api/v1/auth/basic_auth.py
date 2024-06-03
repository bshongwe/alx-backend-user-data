#!/usr/bin/env python3
"""Basic authentication module for the API.
"""
import re
from typing import TypeVar

from models.user import User
from .auth import Auth


class BasicAuth(Auth):
    """Basic authentication class.
    """
    pass
