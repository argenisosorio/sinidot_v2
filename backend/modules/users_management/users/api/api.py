from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List
from django.http import HttpRequest
from modules.users_management.users.api.schemas import UserCreateSchema, UserSchema
from modules.users_management.users.services import user_service


# XXXXXXXX
router = Router()

# Lista de Usuarios (GET)
@router.get("/", response=List[UserSchema])
def list_users(request: HttpRequest):
    return user_service.get_all_users()


# Obtener un Usuario (GET por ID)
@router.get("/{user_id}", response=UserSchema)
def get_user(request: HttpRequest, user_id: int):
    return user_service.get_user(user_id)


# Crear un Usuario (POST)
@router.post("/", response=UserSchema)
def create_user(request: HttpRequest, data: UserCreateSchema):
    return user_service.create_user(data)


# Actualizar un Usuario (PUT)
@router.put("/{user_id}", response=UserSchema)
def update_user(request: HttpRequest, user_id: int, data: UserCreateSchema):
    return user_service.update_user(user_id, data)


# Eliminar un Usuario (DELETE)
@router.delete("/{user_id}")
def delete_user(request: HttpRequest, user_id: int) -> dict[str, str | bool]:
    user_service.delete_user(user_id)
    return {"success": True, "message": f"User {user_id} deleted successfully"}
