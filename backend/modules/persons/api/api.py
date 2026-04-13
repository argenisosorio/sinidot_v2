from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List
from django.http import HttpRequest
from apps.persons.api.schemas import PersonCreateSchema, PersonSchema
from apps.persons.services import person_service


router = Router()

# --- ENDPOINTS (CRUD) ---

# 1. Listar personas (GET)
@router.get("/", response=List[PersonSchema])
def list_persons(request: HttpRequest):
    return person_service.get_all_persons()


# 2. Obtener una persona (GET por ID)
@router.get("/{person_id}", response=PersonSchema)
def get_person(request: HttpRequest, person_id: int):
    return person_service.get_person(person_id)


# 3. Crear una persona (POST)
@router.post("/", response=PersonSchema)
def create_person(request: HttpRequest, data: PersonCreateSchema):
    return person_service.create_person(data)


# 4. Actualizar una persona (PUT)
@router.put("/{person_id}", response=PersonSchema)
def update_person(request: HttpRequest, person_id: int, data: PersonCreateSchema):
    return person_service.update_person(person_id, data)


# 5. Eliminar una persona
@router.delete("/{person_id}")
def delete_person(request: HttpRequest, person_id: int) -> dict[str, str | bool]:
    person_service.delete_person(person_id)
    return {"success": True, "message": f"Person {person_id} deleted successfully"}
