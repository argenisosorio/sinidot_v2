"""
Módulo de API para la gestión de usuarios.

Este módulo expone los endpoints RESTful para las operaciones CRUD de usuarios,
así como los endpoints de autenticación JWT (login, refresh, logout).
"""

from ninja import ModelSchema, Router, Schema
from django.shortcuts import get_object_or_404
from typing import List
from django.http import HttpRequest
from modules.users_management.users.models.user import User
from modules.users_management.users.api.schemas import (
    UserSchema,
    UserCreateSchema,
    UserUpdateSchema,
    RefreshTokenSchema,
)
from modules.users_management.users.services import user_service
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.routers.obtain import obtain_pair_router
from ninja_jwt.tokens import RefreshToken


# =============================================================================
# Inicialización del router
# =============================================================================

router = Router()


# =============================================================================
# Endpoints de autenticación JWT
# =============================================================================

# Se integra el router por defecto de ninja-jwt que proporciona los endpoints:
# - /token/pair     -> Obtener access y refresh token
# - /token/refresh  -> Renovar access token mediante refresh token
# - /token/verify   -> Verificar validez de un token
router.add_router("/token", obtain_pair_router)


# =============================================================================
# Endpoint: Cierre de sesión (Logout)
# =============================================================================

@router.post(
    "/logout",
    auth=JWTAuth(),
    description="Endpoint para cerrar sesión (Invalidar el token)",
)
def logout(request: HttpRequest, data: RefreshTokenSchema) -> dict:
    """
    Cierra la sesión del usuario invalidando su refresh token.

    Args:
        request: Objeto HttpRequest de Django.
        data: Esquema que contiene el refresh token a invalidar.

    Returns:
        Dict con indicador de éxito y mensaje informativo.

    Raises:
        Exception: Captura cualquier error durante la invalidación del token.
    """
    try:
        token = RefreshToken(data.refresh)
        token.blacklist()  # Agrega el token a la lista negra
        return {"success": True, "message": "Logged out successfully"}
    except Exception as e:
        return {"success": False, "message": str(e)}


# =============================================================================
# Operaciones CRUD de Usuarios
# =============================================================================

@router.get("/", response=List[UserSchema])
def list_users(request: HttpRequest) -> List[User]:
    """
    Obtiene la lista completa de usuarios.

    Args:
        request: Objeto HttpRequest de Django.

    Returns:
        Lista de esquemas UserSchema con los datos de todos los usuarios.
    """
    return user_service.get_all_users()


@router.get("/{user_id}", response=UserSchema)
def get_user(request: HttpRequest, user_id: int) -> User:
    """
    Obtiene un usuario específico por su ID.

    Args:
        request: Objeto HttpRequest de Django.
        user_id: Identificador único del usuario.

    Returns:
        Esquema UserSchema con los datos del usuario solicitado.

    Raises:
        Http404: Si el usuario con el ID especificado no existe.
    """
    return user_service.get_user(user_id)


@router.post("/", response=UserSchema)
def create_user(request: HttpRequest, data: UserCreateSchema) -> User:
    """
    Crea un nuevo usuario en el sistema.

    Args:
        request: Objeto HttpRequest de Django.
        data: Esquema con los datos de creación del usuario.

    Returns:
        Esquema UserSchema con los datos del usuario creado.

    Raises:
        ValidationError: Si los datos de entrada no superan las validaciones.
    """
    return user_service.create_user(data)


@router.put("/{user_id}", response=UserSchema)
def update_user(
    request: HttpRequest, user_id: int, data: UserCreateSchema
) -> User:
    """
    Actualiza un usuario existente.

    Args:
        request: Objeto HttpRequest de Django.
        user_id: Identificador único del usuario a actualizar.
        data: Esquema con los datos actualizados del usuario.

    Returns:
        Esquema UserSchema con los datos del usuario actualizado.

    Raises:
        Http404: Si el usuario con el ID especificado no existe.
        ValidationError: Si los datos de entrada no superan las validaciones.
    """
    return user_service.update_user(user_id, data)


@router.delete("/{user_id}")
def delete_user(request: HttpRequest, user_id: int) -> dict:
    """
    Elimina un usuario del sistema.

    Args:
        request: Objeto HttpRequest de Django.
        user_id: Identificador único del usuario a eliminar.

    Returns:
        Dict con indicador de éxito y mensaje de confirmación.

    Raises:
        Http404: Si el usuario con el ID especificado no existe.
    """
    user_service.delete_user(user_id)
    return {
        "success": True,
        "message": f"User {user_id} deleted successfully",
    }
