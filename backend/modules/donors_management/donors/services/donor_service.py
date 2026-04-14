from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import get_object_or_404
from modules.donors_management.donors.dtos.donor_dto import DonorDTO, UpdateDonorDTO
from modules.donors_management.donors.models.donor import Donor


@transaction.atomic
def create_donor(donor_dto: DonorDTO) -> Donor:
    """
    XXXXXXXXXXXXxx
    """
    donor = Donor.objects.create(
        name=donor_dto.name,
        email=donor_dto.email,
        age=donor_dto.age
    )
    return donor


@transaction.atomic
def update_donor(donor_id: int, donor_dto: UpdateDonorDTO) -> Donor:
    """
    Xxxxxxxxxx
    """
    donor = get_object_or_404(Donor, id=donor_id)
    
    # Lisa de campos que se pueden actualizar
    donor_fields = ["name", "email", "age"]
    
    for field in donor_fields:
        value = getattr(donor_dto, field, None)
        # Update only if value is provided (not None and not empty string)
        if value is not None and value != "":
            setattr(donor, field, value)
    
    donor.save()
    return donor


def delete_donor(donor_id: int) -> None:
    """
    xxxxxxxxxxx
    """
    donor = get_object_or_404(Donor, id=donor_id)
    donor.delete()


def get_all_donors() -> list[Donor]:
    """
    xxxxxxxxxx
    """
    return Donor.objects.all().order_by('-created_at')


def get_donor(donor_id: int) -> Donor:
    """
    xxxxxxxxxxx
    """
    return get_object_or_404(Donor, id=donor_id)
