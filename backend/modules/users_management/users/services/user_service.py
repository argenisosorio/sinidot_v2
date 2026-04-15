from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import get_object_or_404
from modules.users_management.users.dtos.user_dto import UserDTO, UpdateUserDTO

User = get_user_model()


@transaction.atomic
def create_user(user_dto: UserDTO) -> User:
    """
    Crea un nuevo usuario.
    """
    user = User.objects.create_user(
        username=user_dto.username,
        email=user_dto.email,
        password=user_dto.password,
        first_name=user_dto.first_name or "",
        last_name=user_dto.last_name or "",
    )
    
    if user_dto.role:
        user.role = user_dto.role
        user.save()
    
    return user


@transaction.atomic
def update_user(user_id: int, user_dto: UpdateUserDTO) -> User:
    """
    Actualiza un usuario existente.
    """
    user = get_object_or_404(User, id=user_id)
    
    # Lista de campos que se pueden actualizar
    user_fields = ["username", "email", "first_name", "last_name", "role"]
    
    for field in user_fields:
        value = getattr(user_dto, field, None)
        if value is not None and value != "":
            setattr(user, field, value)
    
    # Si se proporciona password, actualizarlo de forma segura
    if user_dto.password:
        user.set_password(user_dto.password)
    
    user.save()
    return user


def delete_user(user_id: int) -> None:
    """
    Elimina un usuario.
    """
    user = get_object_or_404(User, id=user_id)
    user.delete()


def get_all_users() -> list[User]:
    """
    Obtiene todos los usuarios ordenados por fecha de creación.
    """
    return User.objects.all().order_by('-date_joined')


def get_user(user_id: int) -> User:
    """
    Obtiene un usuario por su ID.
    """
    return get_object_or_404(User, id=user_id)