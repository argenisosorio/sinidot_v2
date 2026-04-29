<template>
  <div>
    <button class="btn btn-success">
      <NuxtLink
        to="/users/create">
        Registrar usuario
      </NuxtLink>
    </button>

    <br>
    <br>

    <h1>Lista de Usuarios</h1>

    <table class="table table-striped">
      <thead>
        <tr>
          <th>Nombre de usuario</th>
          <th>Correo electrónico</th>
          <th>Nombres</th>
          <th>Apellidos</th>
          <th>Rol</th>
          <th>Creado</th>
          <th class="text-center">Acción</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.username }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.first_name }}</td>
          <td>{{ user.last_name }}</td>
          <td>{{ showRole(user.role) }}</td>
          <td>
            {{ formatDate(user.date_joined) }}
          </td>
          <td class="text-center">
            Editar registro | Ver registro
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import GoBack from '~/components/goBack.vue'

// Proteger esta página con el middleware de autenticación.
definePageMeta({
  middleware: ['auth'],
})

// Importamos la función de utilidad para formatear fechas.
const { formatDate, showRole } = utils()

// Inicializa el acceso a la variable de entorno para la URL base del backend.
const config = useRuntimeConfig()

// Ahora 'apiBase' contiene la URL base de la API configurada en el .env
const apiBase = config.public.apiBase

// Estado global para controlar el loader
const loader = useState('loader')

// Configuramos el título de la página
useHead({
  title: 'Lista de Usuarios',
})

// Llamada a la API de Backend usando una API de prueba real
const { data: response, pending} = await useFetch(`${apiBase}/users/`, {
  lazy: true
})

// Mapeamos los resultados (JSONPlaceholder devuelve un Array directo)
const users = computed(() => response.value || [])

// Observamos 'pending' y asignamos su valor directamente al loader
watch(pending, (newVal) => {
  loader.value = newVal
}, { immediate: true }) // immediate asegura que si empieza cargando, el loader se active de una vez
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse; /* Crucial para que las líneas se unan */
}

table, th, td {
  border: 1px solid black; /* Define el grosor, estilo y color de la rejilla */
}

th, td {
  padding: 8px; /* Espaciado interno para que el texto no toque las líneas */
  text-align: left; /* Alineación del texto */
}

th {
  background-color: #f2f2f2; /* Color de fondo opcional para el encabezado */
}
</style>
