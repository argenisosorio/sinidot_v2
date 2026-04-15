from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from ninja import NinjaAPI
from modules.donors_management.donors.api.api import router as donor_router
from modules.applicants_management.applicants.api.api import router as applicant_router
from modules.users.api.api import router as user_router


# Función de bienvenida.
def home(request):
    return HttpResponse("<h1>Bienvenido al SINIDOT v2</h1>")


# Instancia de la API.
api = NinjaAPI(
    title="SINIDOT v2 API", 
    version="2.0.0",
    description="SINIDOT v2 Endpoints"
)


# Routers de las apps.
api.add_router("/donors/", donor_router)
api.add_router("/applicants/", applicant_router)
api.add_router("/users/", user_router)


# Rutas del proyecto.
urlpatterns = [
    # Ruta raíz
    path('', home),

    # Ruta para Administradores.
    path('admin/', admin.site.urls),

    # Rutas del API de Django Ninja.
    path("api/", api.urls),
]
