from django.urls import path
from modules.donors_management.donors.controllers import donor_controller
from modules.donors_management.donors.controllers.donor_controller import (
    index,
    create,
    edit,
    store,
    delete,
    update,
)

app_name = "donors"

urlpatterns = [
    path("", index, name="index"),
    path("create/", create, name="create"),
    path("store/", store, name="store"),
    path("edit/<int:donor_id>/", edit, name="edit"),
    path("delete/<int:donor_id>/", delete, name="delete"),
    path("update/<int:donor_id>/", update, name="update"),
]
