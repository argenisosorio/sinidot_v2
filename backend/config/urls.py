from django.contrib import admin
from django.urls import include, path
from ninja import NinjaAPI
from modules.donors_management.donors.api.api import router as donor_router


# Instanciamos la API
api = NinjaAPI(title="Donors Endpoints")

# Añadimos los routers de cada app
api.add_router("/donors/", donor_router)

urlpatterns = [
    # Admin route
    path('admin/', admin.site.urls),

    # Include the URLs from persons app.
    path('', include('modules.donors_management.donors.urls')),

    # API routes Django Ninja
    path("api/", api.urls),
]
