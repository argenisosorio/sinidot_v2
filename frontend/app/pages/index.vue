<template>
  <div>
    <h1>
      <img
        src="/images/logo.png"
        alt="star"
        class="img-fluid mb-3"
        width="50"
      >
      Bienvenido al Sistema Nacional de Información sobre Donación y Trasplantes (SINIDOT)
    </h1>

    <button 
      class="btn btn-danger mt-4"
      :disabled="isLoggingOut"
      aria-live="polite"
      @click="handleLogout"
    >
      <span v-if="isLoggingOut">Logging out...</span>
      <span v-else>Log out</span>
    </button>

    <div v-if="logoutError" class="alert alert-warning mt-3" role="alert">
      {{ logoutError }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// Protege esta página con el middleware de autenticación.
definePageMeta({
  middleware: ['auth'],
})

// Configura el título de la página.
useHead({
  title: 'SINIDOT'
})

// Initialize runtime config to access the API Base URL
const config = useRuntimeConfig()
const apiBase = config.public.apiBase

const loader = useState('loader')

// Reactive variables for the logout state
const isLoggingOut = ref(false)
const logoutError = ref('')

// Access the cookies
const accessToken = useCookie('access_token')
const refreshToken = useCookie('refresh_token')

onMounted(() => {
  console.log("Activo el loader")
  loader.value = true

  setTimeout(() => {
    loader.value = false
    console.log("Ha pasado 1 segundo y quité el loader")
  }, 1000)
})

// 3. La lógica de cierre de sesión
const handleLogout = async () => {
  // Activar el estado de "cerrando sesión" para mostrar un indicador visual y evitar múltiples clics
  isLoggingOut.value = true
  
  // Limpiar cualquier mensaje de error que pudiera haber quedado de intentos anteriores
  logoutError.value = ''

  try {
    // Verificar que exista un token de refresco antes de intentar cerrar sesión
    if (refreshToken.value) {
      console.log("Intentando cerrar sesión en el backend con refresh token:", refreshToken.value)
      // NOTA: Se usa $fetch nativo en lugar de useApiFetch porque el endpoint de logout
      // espera el token de refresco en el CUERPO de la petición, no en la cabecera.
      // Realizar petición POST al endpoint de logout del backend
      await $fetch(`${apiBase}/users/logout`, {
        method: 'POST',                    // Método HTTP POST
        headers: {
          Authorization: `Bearer ${accessToken.value}`  // Enviar token de acceso en la cabecera
        },
        body: {
          refresh: refreshToken.value      // Enviar token de refresco en el cuerpo de la petición
        }
      })
    }
  } catch (error) {
    // Capturar cualquier error ocurrido durante la petición al backend
    console.error("Error al cerrar sesión en el backend:", error)
    // Mostrar mensaje amigable al usuario indicando que la sesión local se cerrará de todos modos
    logoutError.value = "No se pudo conectar con el servidor, pero tu sesión local ha sido cerrada."
  } finally {
    // Este bloque se ejecuta SIEMPRE, haya ocurrido error o no
    
    // 4. Destruir las cookies locales de forma segura
    accessToken.value = null   // Eliminar token de acceso
    refreshToken.value = null  // Eliminar token de refresco

    // 5. Redirigir al usuario de vuelta a la pantalla de inicio de sesión
    isLoggingOut.value = false           // Desactivar el estado de carga
    await navigateTo('/login')           // Navegar a la ruta de login
  }
}
</script>