from django.contrib import admin
from django.urls import include, path
from ninja import NinjaAPI
from modules.donors_management.donors.api.api import router as donor_router
from modules.applicants_management.applicants.api.api import router as applicant_router


# Instanciamos la API
api = NinjaAPI(
    title="SINIDOT v2 API", 
    version="2.0.0",
    description="SINIDOT v2 Endpoints"
)

# Añadimos los routers de cada app
api.add_router("/donors/", donor_router)
api.add_router("/applicants/", applicant_router)

urlpatterns = [
    # Admin route
    path('admin/', admin.site.urls),

    # API routes Django Ninja
    path("api/", api.urls),
]
