from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST
from modules.users_management.users.dtos.user_dto import UserDTO, UpdateUserDTO
from modules.users_management.users.models.user import User
from modules.users_management.users.requests.create_user import CreateUserRequest
from modules.users_management.users.requests.update_user import UpdateUserRequest
from modules.users_management.users.services import user_service


def index(request):
    users = user_service.get_all_users()
    context = {"users": users}
    return render(request, "users/index.html", context)


@require_GET
def create(request: HttpRequest) -> HttpResponse:
    return render(request, "users/create_user.html")


@require_GET
def edit(request: HttpRequest, user_id: int) -> HttpResponse:
    user = user_service.get_user(user_id)
    context = {"user": user}
    return render(request, "users/update.html", context)


@require_POST
def store(request: HttpRequest) -> HttpResponse:
    # Formulario para validar los datos de entrada y crear un DTO para el servicio
    form = CreateUserRequest(request.POST)

    # Si los datos no son válidos, devolver un error con los mensajes de validación
    if not form.is_valid():
        return HttpResponse(f"Invalid data: {form.errors}", status=400)

    user_dto = UserDTO(**form.cleaned_data)
    user_service.create_user(user_dto)
    return redirect(reverse("users:index"))


@require_POST
def delete(request: HttpRequest, user_id: int) -> HttpResponse:
    user_service.delete_user(user_id)
    return redirect(reverse("users:index"))


@require_POST   
def update(request: HttpRequest, user_id: int) -> HttpResponse:
    user_data = UpdateUserRequest(request.POST)
    if not user_data.is_valid():
        return HttpResponse(f"Invalid data: {user_data.errors}", status=400)

    user_dto = UpdateUserDTO(**user_data.cleaned_data)
    user_service.update_user(user_id, user_dto)
    return redirect(reverse("users:index"))
