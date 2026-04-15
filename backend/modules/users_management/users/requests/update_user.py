from django import forms
from modules.donors_management.donors.models.donor import Donor
from django.contrib.auth.forms import UserChangeForm


# Formulario especializado para la actualización de datos de usuarios existentes
class CustomUserChangeForm(UserChangeForm): # Se recomienda heredar de UserChangeForm para mantener validaciones de password
    # Clase interna para configurar la metadata del formulario de edición
    class Meta:
        # Vinculamos nuevamente con nuestro modelo User personalizado
        model = User
        # Definimos qué campos serán editables desde la interfaz (ej. el panel de administración)
        fields = ("username", "email", "first_name", "last_name", "role")
