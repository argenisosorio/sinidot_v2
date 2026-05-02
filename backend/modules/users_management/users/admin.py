"""
Configuración del panel de administración para el módulo de usuarios.

Registra el modelo User en el panel de administración de Django para
permitir su gestión desde la interfaz administrativa.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from modules.users_management.users.models.user import User


# =============================================================================
# Configuración del administrador para el modelo User
# =============================================================================

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Configuración personalizada del panel de administración para el modelo User.

    Hereda de BaseUserAdmin para mantener todas las funcionalidades estándar
    del administrador de usuarios de Django (gestión de contraseñas, permisos,
    grupos, etc.) y añade el campo 'role' a las secciones correspondientes.

    Attributes:
        list_display: Campos mostrados en la vista de lista.
        fieldsets: Estructura de campos en la vista de detalle/edición.
        add_fieldsets: Estructura de campos en la vista de creación.
    """

    # Campos que se muestran en la lista de usuarios del panel admin
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_staff",
        "is_active",
        "date_joined",
    )

    # Campos que se pueden usar para filtrar en el panel lateral
    list_filter = (
        "is_staff",
        "is_active",
        "is_superuser",
        "role",
        "date_joined",
    )

    # Campos por los que se puede buscar en el panel admin
    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
    )

    # Ordenamiento por defecto (los más recientes primero)
    ordering = ("-date_joined",)

    # Configuración de los campos en la vista de edición de usuario
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Información personal", {
            "fields": (
                "first_name",
                "last_name",
                "email",
                "role",
            )
        }),
        ("Permisos", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Fechas importantes", {
            "fields": (
                "last_login",
                "date_joined",
            )
        }),
    )

    # Configuración de los campos en la vista de creación de usuario
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username",
                "email",
                "first_name",
                "last_name",
                "role",
                "password1",
                "password2",
            ),
        }),
    )
