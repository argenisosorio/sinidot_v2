from dataclasses import dataclass
from typing import Optional

# Objeto de transferencia de datos (DTO) para crear un nuevo solicitante
@dataclass(frozen=True)
class ApplicantDTO:
    name: str
    email: str
    age: int


# Objeto de transferencia de datos (DTO) para actualizar un solicitante existente
@dataclass(frozen=True)
class UpdateApplicantDTO:
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None