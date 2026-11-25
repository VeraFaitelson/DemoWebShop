"""User data model for Demo Web Shop authorization and registration"""

from dataclasses import dataclass, field


@dataclass
class User:
    """Data model representing a customer entity"""

    name: str = ""
    lastname: str = ""
    email: str = ""
    password: str = field(default="", repr=False)
