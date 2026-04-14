from django import forms
from django.core.validators import MinLengthValidator, EmailValidator, MinValueValidator, MaxValueValidator
from modules.applicants_management.applicants.models.applicant import Applicant


class UpdateApplicantRequest(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        validators=[MinLengthValidator(2)],
        error_messages={
            'max_length': 'El nombre no puede exceder los 100 caracteres',
            'min_length': 'El nombre debe tener al menos 2 caracteres'
        }
    )

    email = forms.EmailField(
        required=False,
        validators=[EmailValidator()],
        error_messages={
            'invalid': 'Ingrese un correo electrónico válido'
        }
    )
    
    age = forms.IntegerField(
        required=False,
        validators=[
            MinValueValidator(1, message='La edad debe ser mayor a 0'),
            MaxValueValidator(120, message='La edad no puede ser mayor a 120 años')
        ],
        error_messages={
            'invalid': 'Ingrese una edad válida'
        }
    )

    def clean_email(self):
        """
        Validar que el correo electrónico sea único (excluyendo al solicitante actual).
        """
        email = self.cleaned_data.get("email")

        # Si no se proporciona un nuevo correo electrónico, no es necesario validarlo
        if not email:
            return email

        # Nota: La validación de unicidad que excluya al solicitante actual
        # debe realizarse en el servicio, ya que aquí no tenemos acceso al ID.
        return email

    def clean_name(self):
        """Validar que el nombre no contenga caracteres inválidos."""
        name = self.cleaned_data.get("name")
        
        # Si no se proporciona un nuevo nombre, no es necesario validarlo
        if not name:
            return name

        if not all(c.isalpha() or c.isspace() for c in name):
            raise forms.ValidationError("El nombre solo puede contener letras y espacios.")

        return name.strip()
