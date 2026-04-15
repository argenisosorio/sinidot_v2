from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class UserDTO:
    username: str
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = None


@dataclass(frozen=True)
class UpdateUserDTO:
    username: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = None
    password: Optional[str] = None
