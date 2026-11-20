"""Helper functions to generate random anonymized test data"""

import uuid

from conftest import DEFAULT_USER
from models.user import User


def generate_unique_email() -> str:
    """Generates a unique email address for registration and negative login tests"""
    random_part = uuid.uuid4().hex[:8]
    return f"qa_shop_{random_part}@gmail.com"


def generate_user() -> User:
    """Creates a new valid User with a unique email"""
    return User(
        name=DEFAULT_USER.name,
        lastname=DEFAULT_USER.lastname,
        email=generate_unique_email(),
        password=DEFAULT_USER.password,
    )
