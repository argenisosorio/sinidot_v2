from ninja import Field, Router, ModelSchema, Schema
from modules.users_management.users.models import User


class RefreshTokenSchema(Schema):
    """Schema para refrescar el token JWT"""

    refresh: str = Field(description="Refresh token JWT")


class UserSchema(ModelSchema):
    """Schema para devolver datos del usuario (Output)"""
    class Meta:
        model = User
        # Listamos los campos definidos en tus formularios
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'role',
            'date_joined'
        ]


class UserCreateSchema(Schema):
    """Schema para crear un usuario (Input)"""
    username: str
    email: str
    password: str
    first_name: str = None
    last_name: str = None
    role: str = "user" # Valor por defecto si no se envía


class UserUpdateSchema(Schema):
    """Schema para actualizar un usuario (campos opcionales)"""
    email: str = None
    first_name: str = None
    last_name: str = None
    role: str = None
