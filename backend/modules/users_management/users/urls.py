"""
URLs del módulo de gestión de usuarios.

Define las rutas para autenticación (login, logout, signup), recuperación
de contraseña, cambio de contraseña y operaciones CRUD de usuarios.
"""

from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from modules.users_management.users import views
from modules.users_management.users.views import (
    SignUpView,
    UserCreateView,
    UserDeleteView,
    UserDetailView,
    UserListView,
    UserUpdateView,
)

# Nombre del espacio de nombres para las URLs de este módulo.
app_name = "users"

urlpatterns = [
    # =========================================================================
    # URLs de autenticación (Login / Logout / Signup)
    # =========================================================================
    path(
        "login/",
        views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logoutt/",
        views.LogoutView.as_view(),
        name="logout",
    ),
    path(
        "signup/",
        SignUpView.as_view(template_name="users/signup.html"),
        name="signup",
    ),

    # =========================================================================
    # URLs de recuperación de contraseña (Password Reset)
    # =========================================================================
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="users/password_reset_form.html",
            email_template_name="users/password_reset_email.html",
            html_email_template_name="users/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),

    # =========================================================================
    # URLs de cambio de contraseña (Password Change)
    # =========================================================================
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="users/password_change_form.html",
            success_url=reverse_lazy("users:password_change_done"),
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html"
        ),
        name="password_change_done",
    ),

    # =========================================================================
    # URLs CRUD de usuarios (Gestión administrativa)
    # =========================================================================
    path(
        "",
        UserListView.as_view(template_name="users/user_list.html"),
        name="user_list",
    ),
    path(
        "<int:pk>/",
        UserDetailView.as_view(template_name="users/user_detail.html"),
        name="user_detail",
    ),
    path(
        "create/",
        UserCreateView.as_view(template_name="users/user_form.html"),
        name="user_create",
    ),
    path(
        "update/<int:pk>/",
        UserUpdateView.as_view(template_name="users/user_form.html"),
        name="user_update",
    ),
    path(
        "delete/<int:pk>/",
        UserDeleteView.as_view(
            template_name="users/user_confirm_delete.html"
        ),
        name="user_delete",
    ),
]
