from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST
from modules.donors_management.donors.dtos.donor_dto import DonorDTO, UpdateDonorDTO
from modules.donors_management.donors.models.donor import Donor
from modules.donors_management.donors.requests.create_donor import CreateDonorRequest
from modules.donors_management.donors.requests.update_donor import UpdateDonorRequest
from modules.donors_management.donors.services import donor_service


def index(request):
    donors = donor_service.get_all_donors()
    context = {"donors": donors}
    return render(request, "donors/index.html", context)


@require_GET
def create(request: HttpRequest) -> HttpResponse:
    return render(request, "donors/create_donor.html")


@require_GET
def edit(request: HttpRequest, donor_id: int) -> HttpResponse:
    donor = donor_service.get_donor(donor_id)
    context = {"donor": donor}
    return render(request, "donors/update.html", context)


@require_POST
def store(request: HttpRequest) -> HttpResponse:
    # Formulario para validar los datos de entrada y crear un DTO para el servicio
    form = CreateDonorRequest(request.POST)

    # Si los datos no son válidos, devolver un error con los mensajes de validación
    if not form.is_valid():
        return HttpResponse(f"Invalid data: {form.errors}", status=400)

    donor_dto = DonorDTO(**form.cleaned_data)
    donor_service.create_donor(donor_dto)
    return redirect(reverse("donors:index"))


@require_POST
def delete(request: HttpRequest, donor_id: int) -> HttpResponse:
    donor_service.delete_donor(donor_id)
    return redirect(reverse("donors:index"))


@require_POST   
def update(request: HttpRequest, donor_id: int) -> HttpResponse:
    donor_data = UpdateDonorRequest(request.POST)
    if not donor_data.is_valid():
        return HttpResponse(f"Invalid data: {donor_data.errors}", status=400)

    donor_dto = UpdateDonorDTO(**donor_data.cleaned_data)
    donor_service.update_donor(donor_id, donor_dto)
    return redirect(reverse("donors:index"))
