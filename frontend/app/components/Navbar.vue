<template>
  <div class="mb-3">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon" />
        </button>
        <div id="navbarSupportedContent" class="collapse navbar-collapse">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <NuxtLink class="nav-link" to="https://fundavene.gob.ve/">
                FUNDAVENE
              </NuxtLink>
            </li>
            <li class="nav-item">
              <NuxtLink class="nav-link" to="/">INICIO</NuxtLink>
            </li>
            <li class="nav-item">
              <NuxtLink class="nav-link" to="/users">GESTIÓN DE USUARIOS</NuxtLink>
            </li>
            <li class="nav-item dropdown">
              <a
                id="navbarDropdown"
                class="nav-link dropdown-toggle"
                href="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                USER
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li>
                  <a
                    class="dropdown-item"
                    href="#"
                    @click="handleLogout"
                  >
                    Salir
                  </a>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script setup>
// Initialize runtime config to access the API Base URL
const config = useRuntimeConfig()
const apiBase = config.public.apiBase

// Reactive variables for the logout state
const isLoggingOut = ref(false)
const logoutError = ref('')

// Access the cookies
const accessToken = useCookie('access_token')
const refreshToken = useCookie('refresh_token')

// La lógica de cierre de sesión
const handleLogout = async () => {
  // Activar el estado de "cerrando sesión"
  isLoggingOut.value = true

  // Limpiar cualquier mensaje de error
  logoutError.value = ''

  try {
    // Verificar que exista un token de refresco
    if (refreshToken.value) {
      console.log("Intentando cerrar sesión en el backend con refresh token:", refreshToken.value)

      await $fetch(`${apiBase}/users/logout`, {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${accessToken.value}`
        },
        body: {
          refresh: refreshToken.value
        }
      })
    }
  } catch (error) {
    console.error("Error al cerrar sesión en el backend:", error)
    logoutError.value = "No se pudo conectar con el servidor, pero tu sesión local ha sido cerrada."
  } finally {
    // Eliminar cookies locales
    accessToken.value = null
    refreshToken.value = null

    // Desactivar estado de carga y redirigir
    isLoggingOut.value = false
    await navigateTo('/login')
  }
}

// Exponer handleLogout al template
defineExpose({ handleLogout })
</script>