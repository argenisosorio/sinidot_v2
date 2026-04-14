from dataclasses import dataclass
from typing import Optional

# Objeto de transferencia de datos (DTO) para crear un nuevo donante
@dataclass(frozen=True)
class DonorDTO:
    name: str
    email: str
    age: int


# Objeto de transferencia de datos (DTO) para actualizar un donante existente
@dataclass(frozen=True)
class UpdateDonorDTO:
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
