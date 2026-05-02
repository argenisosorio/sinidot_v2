"""
Configuración de la aplicación de gestión de usuarios.

Define la configuración de la app 'users' dentro del módulo de gestión
de usuarios del sistema.
"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Configuración de la aplicación de usuarios.

    Esta clase configura la aplicación 'users' estableciendo el tipo de
    clave primaria por defecto, la ruta de importación y la etiqueta
    corta para referenciar la app en el proyecto.
    """

    # Define el tipo de dato por defecto para las llaves primarias (IDs)
    # de los modelos. BigAutoField es un entero de 64 bits que soporta
    # hasta 9.2 cuatrillones de registros.
    default_auto_field = "django.db.models.BigAutoField"

    # Ruta completa de importación de la aplicación.
    # Corresponde a la ubicación física del módulo en el proyecto.
    name = "modules.users_management.users"

    # Etiqueta corta que Django usa para identificar la app internamente.
    # Al definirla como 'users', se puede usar AUTH_USER_MODEL = "users.User"
    # en el archivo settings.py para establecer el modelo de usuario
    # personalizado como el modelo de autenticación principal del sistema.
    label = "users"
