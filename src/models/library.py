from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class CreateLibrary:
    name: str
    address: str
    phone: Optional[str]
    email: Optional[str]
