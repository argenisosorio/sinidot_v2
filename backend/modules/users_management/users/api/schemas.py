from modules.users_management.users.models.user import User
from ninja import ModelSchema, Schema

# --- SCHEMAS ---

class UserSchema(ModelSchema):
    """
    Schema para devolver datos del usuario (Output)
    """
    class Meta:
        model = User
        # Listamos los campos definidos en tus formularios
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'role'
        ]


class UserCreateSchema(Schema):
    """
    Schema para crear un usuario (Input)
    """
    username: str
    email: str
    password: str
    first_name: str = None
    last_name: str = None
    role: str = "USR" # Valor por defecto si no se envía


class UserUpdateSchema(Schema):
    """
    Schema para actualizar un usuario (campos opcionales)
    """
    email: str = None
    first_name: str = None
    last_name: str = None
    role: str = None
