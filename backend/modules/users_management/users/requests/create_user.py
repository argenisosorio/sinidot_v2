from django import forms
from django.core.validators import MinLengthValidator, EmailValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserRequest(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        validators=[MinLengthValidator(3)],
        error_messages={
            'required': 'El nombre de usuario es obligatorio',
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
        required=True,
        validators=[EmailValidator()],
        error_messages={
            'required': 'El correo electrónico es obligatorio',
            'invalid': 'Ingrese un correo electrónico válido'
        }
    )
    
    password = forms.CharField(
        required=True,
        min_length=8,
        widget=forms.PasswordInput,
        error_messages={
            'required': 'La contraseña es obligatoria',
            'min_length': 'La contraseña debe tener al menos 8 caracteres'
        }
    )
    
    confirm_password = forms.CharField(
        required=True,
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
        Validar que el username sea único.
        """
        username = self.cleaned_data.get("username")
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Ya existe un usuario con este nombre de usuario.")
        
        return username

    def clean_email(self):
        """
        Validar que el correo electrónico sea único.
        """
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con este correo electrónico.")

        return email
    
    def clean(self):
        """
        Validar que las contraseñas coincidan.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        return cleaned_data