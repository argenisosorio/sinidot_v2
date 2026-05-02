"""
Módulo de Data Transfer Objects (DTOs) para la gestión de usuarios.

Define las estructuras de datos inmutables que se utilizan para transferir
información entre las capas de la aplicación (API -> Servicio -> Repositorio).
"""

from dataclasses import dataclass
from typing import Optional


# =============================================================================
# DTO para creación de usuarios
# =============================================================================

@dataclass(frozen=True)
class UserDTO:
    """
    DTO para la creación de un nuevo usuario.

    Este objeto se utiliza para transferir los datos desde el endpoint de
    creación hasta el servicio que crea el usuario. Es inmutable para evitar
    modificaciones accidentales durante el proceso.

    Attributes:
        username: Nombre de usuario único para autenticación.
        email: Correo electrónico único del usuario.
        password: Contraseña en texto plano (será hasheada en el servicio).
        first_name: Nombre(s) del usuario (opcional).
        last_name: Apellido(s) del usuario (opcional).
        role: Rol del usuario, ej: 'ADM', 'USR' (opcional).
    """
    username: str
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = None


# =============================================================================
# DTO para actualización de usuarios
# =============================================================================

@dataclass(frozen=True)
class UpdateUserDTO:
    """
    DTO para la actualización parcial de un usuario existente.

    Todos los campos son opcionales para permitir actualizaciones parciales.
    Solo los campos que no sean None serán actualizados en el servicio.

    Attributes:
        username: Nuevo nombre de usuario (opcional).
        email: Nuevo correo electrónico (opcional).
        first_name: Nuevo nombre(s) del usuario (opcional).
        last_name: Nuevo apellido(s) del usuario (opcional).
        role: Nuevo rol del usuario (opcional).
        password: Nueva contraseña (opcional, será hasheada).
    """
    username: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = None
    password: Optional[str] = None
