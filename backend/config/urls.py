"""
Configuración principal de URLs y API del proyecto SINIDOT v2.

Define las rutas principales del proyecto, incluyendo la API REST
con Django Ninja y el panel de administración de Django.
"""

from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from ninja import NinjaAPI
from modules.donors_management.donors.api.api import router as donor_router
from modules.applicants_management.applicants.api.api import router as applicant_router
from modules.users_management.users.api.api import router as user_router


# =============================================================================
# Vistas básicas (no-API)
# =============================================================================

def home(request) -> HttpResponse:
    """
    Vista de la página de bienvenida del proyecto.

    Args:
        request: Objeto HttpRequest de Django.

    Returns:
        Respuesta HTML con el mensaje de bienvenida del sistema.
    """
    return HttpResponse("<h1>Bienvenido al SINIDOT v2</h1>")


# =============================================================================
# Configuración de la API con Django Ninja
# =============================================================================

# Instancia principal de la API con metadatos documentados.
api = NinjaAPI(
    title="SINIDOT v2 API",
    version="2.0.0",
    description="SINIDOT v2 Endpoints",
)


# Registro de los routers de cada módulo de la aplicación.
api.add_router("/donors", donor_router)       # Endpoints para donantes
api.add_router("/applicants", applicant_router)  # Endpoints para solicitantes
api.add_router("/users", user_router)         # Endpoints para usuarios


# =============================================================================
# Configuración de URLs del proyecto
# =============================================================================

urlpatterns = [
    # Ruta raíz del sistema (página de bienvenida)
    path("", home),

    # Panel de administración de Django para gestión interna
    path("admin/", admin.site.urls),

    # Endpoints de la API REST bajo el prefijo /api/
    path("api/", api.urls),
]
