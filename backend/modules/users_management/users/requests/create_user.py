"""
Formularios personalizados para la gestión de usuarios.

Define formularios de Django utilizados en vistas basadas en clases o
funciones para la creación y validación de usuarios.
"""

from django import forms
from modules.donors_management.donors.models.donor import Donor
from django.contrib.auth.forms import UserCreationForm


# =============================================================================
# Formulario de registro de usuarios (Creación)
# =============================================================================

class CustomUserCreationForm(UserCreationForm):
    """
    Formulario especializado para el registro de nuevos usuarios en el sistema.

    Hereda de UserCreationForm de Django, que ya proporciona validación
    de contraseñas (confirmación, complejidad básica). Se personaliza
    para incluir campos adicionales del modelo User.

    Attributes:
        Los campos se definen mediante la clase Meta.

    Note:
        Este formulario se utiliza principalmente en la vista de registro
        (signup) para la creación de cuentas de usuario regulares.
        Los administradores utilizan formularios separados.
    """

    class Meta:
        """
        Configuración interna del formulario.

        Attributes:
            model: Modelo asociado al formulario (User personalizado).
            fields: Campos del modelo que se incluyen en el formulario.
        """
        # Indicamos que este formulario trabajará con nuestro modelo User
        # personalizado (importado indirectamente a través de get_user_model)
        model = User

        # Definimos los campos específicos que se mostrarán en el formulario
        # de creación. Los campos 'password1' y 'password2' son añadidos
        # automáticamente por UserCreationForm.
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "role",
        )
