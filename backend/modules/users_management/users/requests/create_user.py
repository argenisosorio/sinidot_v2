from django import forms
from modules.donors_management.donors.models.donor import Donor
from django.contrib.auth.forms import UserCreationForm


# Formulario especializado para el registro de nuevos usuarios en el sistema
class CustomUserCreationForm(UserCreationForm):
    # Clase interna para configurar la relación entre el formulario y el modelo
    class Meta:
        # Indicamos que este formulario trabajará con nuestro modelo User personalizado
        model = User
        # Definimos los campos específicos que se mostrarán en el formulario de creación
        fields = ("username", "email", "first_name", "last_name", "role")
