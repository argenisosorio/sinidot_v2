from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from modules.users_management.users.models.user import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    # Añadimos el campo role a los formularios del admin
    fieldsets = UserAdmin.fieldsets + (
        ("Información Adicional", {"fields": ("role",)}),
    )
