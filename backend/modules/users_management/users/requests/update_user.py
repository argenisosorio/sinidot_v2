"""
Formulario para la edición de usuarios existentes.

Define formularios personalizados utilizados en el panel de administración
y vistas de perfil para la actualización de datos de usuarios.
"""

from django import forms
from modules.donors_management.donors.models.donor import Donor
from django.contrib.auth.forms import UserChangeForm


# =============================================================================
# Formulario de edición de usuarios
# =============================================================================

class CustomUserChangeForm(UserChangeForm):
    """
    Formulario especializado para la actualización de datos de usuarios existentes.

    Hereda de UserChangeForm de Django, que mantiene las validaciones
    de contraseña y la gestión segura de la misma. Se recomienda usar esta
    clase base en lugar de forms.ModelForm directamente para preservar
    la lógica de seguridad de contraseñas.

    Attributes:
        Los campos se definen mediante la clase Meta.

    Note:
        Este formulario se utiliza principalmente en el panel de administración
        de Django y en vistas de perfil de usuario para permitir la edición
        de datos sin comprometer la seguridad de las contraseñas.
    """
    class Meta:
        """
        Configuración interna del formulario de edición.

        Attributes:
            model: Modelo asociado al formulario (User personalizado).
            fields: Campos del modelo que se incluyen en el formulario de edición.
        """
        # Vinculamos nuevamente con nuestro modelo User personalizado
        model = User

        # Definimos qué campos serán editables desde la interfaz
        # (ej. el panel de administración o vistas de perfil)
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "role",
        )
