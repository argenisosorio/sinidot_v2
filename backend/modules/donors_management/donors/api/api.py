from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List
from django.http import HttpRequest
from modules.donors_management.donors.api.schemas import DonorCreateSchema, DonorSchema
from modules.donors_management.donors.services import donor_service


# XXXXXXXX
router = Router()

# Lista de Donantes (GET)
@router.get("/", response=List[DonorSchema])
def list_donors(request: HttpRequest):
    return donor_service.get_all_donors()


# Obtener un Donante (GET por ID)
@router.get("/{donor_id}", response=DonorSchema)
def get_donor(request: HttpRequest, donor_id: int):
    return donor_service.get_donor(donor_id)


# Crear un Donante (POST)
@router.post("/", response=DonorSchema)
def create_donor(request: HttpRequest, data: DonorCreateSchema):
    return donor_service.create_donor(data)


# Actualizar un Donante (PUT)
@router.put("/{donor_id}", response=DonorSchema)
def update_donor(request: HttpRequest, donor_id: int, data: DonorCreateSchema):
    return donor_service.update_donor(donor_id, data)


# Eliminar un Donante
@router.delete("/{donor_id}")
def delete_donor(request: HttpRequest, donor_id: int) -> dict[str, str | bool]:
    donor_service.delete_donor(donor_id)
    return {"success": True, "message": f"Donor {donor_id} deleted successfully"}
