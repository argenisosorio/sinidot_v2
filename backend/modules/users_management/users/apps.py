from django.apps import AppConfig


class UsersConfig(AppConfig):
    # Define el tipo de dato por defecto para las llaves primarias (IDs) de los modelos.
    default_auto_field = 'django.db.models.BigAutoField'

    # Ruta completa de importación de de la aplicación.
    name = 'modules.users_management.users'

    """
    El nombre corto que Django usará para identificar la app internamente. Al
    definirlo como 'users' se puedes usar AUTH_USER_MODEL = "users.User" en el
    settings.
    """
    label = 'users'
