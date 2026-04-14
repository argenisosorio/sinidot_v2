from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import get_object_or_404
from modules.applicants_management.applicants.dtos.applicant_dto import ApplicantDTO, UpdateApplicantDTO
from modules.applicants_management.applicants.models.applicant import Applicant


@transaction.atomic
def create_applicant(applicant_dto: ApplicantDTO) -> Applicant:
    """
    Crea un nuevo solicitante en la base de datos.
    """
    applicant = Applicant.objects.create(
        name=applicant_dto.name,
        email=applicant_dto.email,
        age=applicant_dto.age
    )
    return applicant


@transaction.atomic
def update_applicant(applicant_id: int, applicant_dto: UpdateApplicantDTO) -> Applicant:
    """
    Actualiza los datos de un solicitante existente.
    """
    applicant = get_object_or_404(Applicant, id=applicant_id)
    
    # Lista de campos que se pueden actualizar
    applicant_fields = ["name", "email", "age"]
    
    for field in applicant_fields:
        value = getattr(applicant_dto, field, None)
        # Actualizar solo si se proporciona un valor (no None y no cadena vacía)
        if value is not None and value != "":
            setattr(applicant, field, value)
    
    applicant.save()
    return applicant


def delete_applicant(applicant_id: int) -> None:
    """
    Elimina un solicitante de la base de datos.
    """
    applicant = get_object_or_404(Applicant, id=applicant_id)
    applicant.delete()


def get_all_applicants() -> list[Applicant]:
    """
    Retorna todos los solicitantes ordenados por fecha de creación descendente.
    """
    return Applicant.objects.all().order_by('-created_at')


def get_applicant(applicant_id: int) -> Applicant:
    """
    Retorna un solicitante específico por su ID.
    """
    return get_object_or_404(Applicant, id=applicant_id)
