"""
Módulo de esquemas (schemas) para la gestión de usuarios.

Define los datos de entrada y salida para las operaciones CRUD de usuarios, así
como los esquemas de autenticación JWT. Utiliza Pydantic para la validación
automática de tipos y formatos.
"""

from ninja import Field, Router, ModelSchema, Schema
from modules.users_management.users.models import User


# =============================================================================
# Esquemas de Autenticación (JWT)
# =============================================================================

class RefreshTokenSchema(Schema):
    """
    Esquema para la operación de refresco de token JWT.

    Este esquema se utiliza como entrada (input) en el endpoint de logout para
    recibir el refresh token que será invalidado.

    Attributes:
        refresh: Token JWT de refresco que será agregado a la lista negra.
    """
    refresh: str = Field(description="Refresh token JWT")


# =============================================================================
# Esquemas de Salida (Response)
# =============================================================================

class UserSchema(ModelSchema):
    """
    Esquema de salida para devolver datos de usuarios.

    Este esquema se utiliza en los endpoints de respuesta GET (listado y
    detalle) para exponer únicamente los campos seguros y necesarios del
    usuario. Contraseñas y datos sensibles quedan ocultos.

    Attributes:
        id: Identificador único del usuario.
        username: Nombre de usuario para autenticación.
        email: Correo electrónico del usuario.
        first_name: Nombre(s) del usuario.
        last_name: Apellido(s) del usuario.
        role: Rol del usuario (ADM, USR, etc.).
        date_joined: Fecha de registro en el sistema.
    """
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'role',
            'date_joined',
        ]


# =============================================================================
# Esquemas de Entrada (Request)
# =============================================================================

class UserCreateSchema(Schema):
    """
    Esquema de entrada para la creación de usuarios.

    Este esquema define los campos requeridos para registrar un nuevo usuario.
    El campo 'role' tiene un valor por defecto 'USR' si no se proporciona
    (creación de usuarios normales).

    Attributes:
        username: Nombre de usuario único para autenticación.
        email: Correo electrónico único del usuario.
        password: Contraseña en texto plano (será hasheada en el servicio).
        first_name: Nombre(s) del usuario (opcional, default: None).
        last_name: Apellido(s) del usuario (opcional, default: None).
        role: Rol del usuario (opcional, default: 'USR').
    """
    username: str
    email: str
    password: str
    first_name: str = None
    last_name: str = None
    role: str = "USR"  # Valor por defecto si no se envía


class UserUpdateSchema(Schema):
    """
    Esquema de entrada para la actualización parcial de usuarios.

    Todos los campos son opcionales para permitir actualizaciones
    parciales (PATCH semantic). Solo se actualizarán los campos
    proporcionados en la solicitud.

    Attributes:
        email: Nuevo correo electrónico del usuario (opcional).
        first_name: Nuevo nombre(s) del usuario (opcional).
        last_name: Nuevo apellido(s) del usuario (opcional).
        role: Nuevo rol del usuario (opcional).
    """
    email: str = None
    first_name: str = None
    last_name: str = None
    role: str = None
