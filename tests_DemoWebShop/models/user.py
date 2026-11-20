"""User data model for Demo Web Shop authorization and registration"""

from dataclasses import dataclass


@dataclass
class User:
    """Data model representing a customer entity"""

    name: str = ""
    lastname: str = ""
    email: str = ""
    password: str = ""
