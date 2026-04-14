from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST
from modules.applicants_management.applicants.dtos.applicant_dto import ApplicantDTO, UpdateApplicantDTO
from modules.applicants_management.applicants.models.applicant import Applicant
from modules.applicants_management.applicants.requests.create_applicant import CreateApplicantRequest
from modules.applicants_management.applicants.requests.update_applicant import UpdateApplicantRequest
from modules.applicants_management.applicants.services import applicant_service


def index(request):
    applicants = applicant_service.get_all_applicants()
    context = {"applicants": applicants}
    return render(request, "applicants/index.html", context)


@require_GET
def create(request: HttpRequest) -> HttpResponse:
    return render(request, "applicants/create_applicant.html")


@require_GET
def edit(request: HttpRequest, applicant_id: int) -> HttpResponse:
    applicant = applicant_service.get_applicant(applicant_id)
    context = {"applicant": applicant}
    return render(request, "applicants/update.html", context)


@require_POST
def store(request: HttpRequest) -> HttpResponse:
    # Formulario para validar los datos de entrada y crear un DTO para el servicio
    form = CreateApplicantRequest(request.POST)

    # Si los datos no son válidos, devolver un error con los mensajes de validación
    if not form.is_valid():
        return HttpResponse(f"Invalid data: {form.errors}", status=400)

    applicant_dto = ApplicantDTO(**form.cleaned_data)
    applicant_service.create_applicant(applicant_dto)
    return redirect(reverse("applicants:index"))


@require_POST
def delete(request: HttpRequest, applicant_id: int) -> HttpResponse:
    applicant_service.delete_applicant(applicant_id)
    return redirect(reverse("applicants:index"))


@require_POST   
def update(request: HttpRequest, applicant_id: int) -> HttpResponse:
    applicant_data = UpdateApplicantRequest(request.POST)
    if not applicant_data.is_valid():
        return HttpResponse(f"Invalid data: {applicant_data.errors}", status=400)

    applicant_dto = UpdateApplicantDTO(**applicant_data.cleaned_data)
    applicant_service.update_applicant(applicant_id, applicant_dto)
    return redirect(reverse("applicants:index"))
