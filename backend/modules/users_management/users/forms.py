from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from .models import User
from modules.users_management.users.models.user import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "role")


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "role")
