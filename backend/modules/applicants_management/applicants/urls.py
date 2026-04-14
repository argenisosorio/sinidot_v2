from django.urls import path
from modules.applicants_management.applicants.controllers import applicant_controller
from modules.applicants_management.applicants.controllers.applicant_controller import (
    index,
    create,
    edit,
    store,
    delete,
    update,
)

app_name = "applicants"

urlpatterns = [
    path("", index, name="index"),
    path("create/", create, name="create"),
    path("store/", store, name="store"),
    path("edit/<int:applicant_id>/", edit, name="edit"),
    path("delete/<int:applicant_id>/", delete, name="delete"),
    path("update/<int:applicant_id>/", update, name="update"),
]
