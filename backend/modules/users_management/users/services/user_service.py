"""
Servicios para la gestión de usuarios.

Este módulo contiene la lógica para las operaciones CRUD de usuarios. Utiliza
transacciones atómicas para garantizar la integridad de los datos y maneja la
creación segura de contraseñas mediante el método create_user de Django.
"""

from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import get_object_or_404
from modules.users_management.users.dtos.user_dto import UserDTO, UpdateUserDTO


User = get_user_model()


# =============================================================================
# Operaciones de Consulta (Read)
# =============================================================================

def get_all_users() -> list[User]:
    """
    Obtiene todos los usuarios ordenados por fecha de creación.

    Los usuarios se devuelven ordenados desde el más reciente al más antiguo
    para facilitar la visualización en listados.

    Returns:
        Lista de objetos User ordenados por date_joined descendente.
    """
    return User.objects.all().order_by('-date_joined')


def get_user(user_id: int) -> User:
    """
    Obtiene un usuario por su ID.

    Args:
        user_id: Identificador único del usuario.

    Returns:
        Objeto User correspondiente al ID proporcionado.

    Raises:
        Http404: Si no existe un usuario con el ID especificado.
    """
    return get_object_or_404(User, id=user_id)


# =============================================================================
# Operaciones de Escritura (Create, Update, Delete)
# =============================================================================

@transaction.atomic
def create_user(user_dto: UserDTO) -> User:
    """
    Crea un nuevo usuario en el sistema.

    Utiliza el método create_user de Django que automáticamente hashea la
    contraseña de forma segura. Los campos first_name y last_name son
    opcionales; si no se proporcionan, se asignan como strings vacíos.

    Args:
        user_dto: Objeto DTO con los datos de creación del usuario.

    Returns:
        Objeto User recién creado con todos sus campos.

    Note:
        La operación se ejecuta dentro de una transacción atómica para
        garantizar que todos los cambios persistan o ninguno.
    """
    user = User.objects.create_user(
        username=user_dto.username,
        email=user_dto.email,
        password=user_dto.password,
        first_name=user_dto.first_name or "",
        last_name=user_dto.last_name or "",
    )

    # Si se proporciona un rol, asignarlo al usuario.
    # Esto se hace por separado porque create_user no incluye campos
    # personalizados como 'role'.
    if user_dto.role:
        user.role = user_dto.role
        user.save()

    return user


@transaction.atomic
def update_user(user_id: int, user_dto: UpdateUserDTO) -> User:
    """
    Actualiza un usuario existente.

    Permite actualizar campos específicos sin necesidad de enviar todos
    los datos. La contraseña se actualiza mediante set_password para
    garantizar el hasheo seguro.

    Args:
        user_id: Identificador único del usuario a actualizar.
        user_dto: DTO con los campos a actualizar (solo los no nulos).

    Returns:
        Objeto User actualizado.

    Raises:
        Http404: Si no existe un usuario con el ID especificado.

    Note:
        La operación se ejecuta dentro de una transacción atómica para
        garantizar la consistencia de los datos.
    """
    user = get_object_or_404(User, id=user_id)

    # Lista de campos que se pueden actualizar desde el DTO
    user_fields = ["username", "email", "first_name", "last_name", "role"]

    for field in user_fields:
        value = getattr(user_dto, field, None)
        if value is not None and value != "":
            setattr(user, field, value)

    # Si se proporciona password, actualizarlo de forma segura.
    # Se usa set_password en lugar de asignación directa para aplicar hash.
    if user_dto.password:
        user.set_password(user_dto.password)

    user.save()
    return user


def delete_user(user_id: int) -> None:
    """
    Elimina un usuario del sistema.

    Args:
        user_id: Identificador único del usuario a eliminar.

    Raises:
        Http404: Si no existe un usuario con el ID especificado.

    Note:
        Esta operación es permanente y no se puede deshacer.
    """
    user = get_object_or_404(User, id=user_id)
    user.delete()
