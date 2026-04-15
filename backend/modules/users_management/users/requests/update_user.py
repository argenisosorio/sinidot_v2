from django import forms
from django.core.validators import MinLengthValidator, EmailValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class UpdateUserRequest(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=False,
        validators=[MinLengthValidator(3)],
        error_messages={
            'max_length': 'El nombre de usuario no puede exceder los 150 caracteres',
            'min_length': 'El nombre de usuario debe tener al menos 3 caracteres'
        }
    )
    
    first_name = forms.CharField(
        max_length=30,
        required=False,
        error_messages={
            'max_length': 'El nombre no puede exceder los 30 caracteres'
        }
    )
    
    last_name = forms.CharField(
        max_length=30,
        required=False,
        error_messages={
            'max_length': 'El apellido no puede exceder los 30 caracteres'
        }
    )

    email = forms.EmailField(
        required=False,
        validators=[EmailValidator()],
        error_messages={
            'invalid': 'Ingrese un correo electrónico válido'
        }
    )
    
    password = forms.CharField(
        required=False,
        min_length=8,
        widget=forms.PasswordInput,
        error_messages={
            'min_length': 'La contraseña debe tener al menos 8 caracteres'
        }
    )
    
    confirm_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput,
        error_messages={
            'required': 'Debe confirmar su contraseña'
        }
    )
    
    role = forms.CharField(
        max_length=3,
        required=False,
        error_messages={
            'max_length': 'El rol no puede exceder los 3 caracteres'
        }
    )
    
    def clean_username(self):
        """
        Validar que el username sea único (excepto el usuario actual).
        Nota: Esta validación necesita el user_id, se puede hacer en la vista
        """
        return self.cleaned_data.get("username")
    
    def clean_email(self):
        """
        Validar que el correo electrónico sea único (excepto el usuario actual).
        Nota: Esta validación necesita el user_id, se puede hacer en la vista
        """
        return self.cleaned_data.get("email")
    
    def clean(self):
        """
        Validar que las contraseñas coincidan si se proporcionan.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        return cleaned_data
