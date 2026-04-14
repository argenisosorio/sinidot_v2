from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List
from django.http import HttpRequest
from modules.applicants_management.applicants.api.schemas import ApplicantCreateSchema, ApplicantSchema
from modules.applicants_management.applicants.services import applicant_service


# XXXXXXXX
router = Router()

# Lista de Solicitantes (GET)
@router.get("/", response=List[ApplicantSchema])
def list_applicants(request: HttpRequest):
    return applicant_service.get_all_applicants()


# Obtener un Solicitante (GET por ID)
@router.get("/{applicant_id}", response=ApplicantSchema)
def get_applicant(request: HttpRequest, applicant_id: int):
    return applicant_service.get_applicant(applicant_id)


# Crear un Solicitante (POST)
@router.post("/", response=ApplicantSchema)
def create_applicant(request: HttpRequest, data: ApplicantCreateSchema):
    return applicant_service.create_applicant(data)


# Actualizar un Solicitante (PUT)
@router.put("/{applicant_id}", response=ApplicantSchema)
def update_applicant(request: HttpRequest, applicant_id: int, data: ApplicantCreateSchema):
    return applicant_service.update_applicant(applicant_id, data)


# Eliminar un Solicitante
@router.delete("/{applicant_id}")
def delete_applicant(request: HttpRequest, applicant_id: int) -> dict[str, str | bool]:
    applicant_service.delete_applicant(applicant_id)
    return {"success": True, "message": f"Applicant {applicant_id} deleted successfully"}
