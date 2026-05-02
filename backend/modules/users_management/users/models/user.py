"""
Modelo de usuario personalizado.

Extiende el modelo AbstractUser de Django para agregar campos adicionales
como el rol del usuario dentro del sistema.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Modelo personalizado de usuario.

    Hereda todas las funcionalidades del modelo User de Django y agrega
    un campo 'role' para la gestión de permisos y roles personalizados.
    Este modelo se utiliza como el modelo de autenticación principal del
    sistema.

    Attributes:
        role: Rol del usuario dentro de la aplicación.
    """
    role = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        help_text="Rol del usuario dentro de la aplicación",
    )

    def __str__(self) -> str:
        """
        Representación en string del usuario.

        Returns:
            Nombre de usuario (username) como representación legible.
        """
        return self.username
