<template>
  <div>
    <GoBack />
    <h1>Registro de usuario</h1>

    <form @submit.prevent="saveUser">
      <div class="mb-3">
        <label class="form-label">
          Nombre de usuario
        </label>
        <input
          v-model="form.username"
          type="text"
          class="form-control"
          required
        >
      </div>

      <div class="mb-3">
        <label class="form-label">Correo electrónico</label>
        <input
          v-model="form.email"
          type="email"
          class="form-control"
          required
        >
      </div>

      <div class="mb-3">
        <label class="form-label">Nombres</label>
        <input
          v-model="form.first_name"
          type="text"
          class="form-control"
          required
        >
      </div>

      <div class="mb-3">
        <label class="form-label">Apellidos</label>
        <input
          v-model="form.last_name"
          type="text"
          class="form-control"
          required
        >
      </div>

      <div class="mb-3">
        <label class="form-label">Rol</label>
        <select
          v-model="form.role"
          class="form-control"
          required
        >
          <option value="">--- Seleccione ---</option>  
          <option value="ADM">Administrador</option>
          <option value="SUP">Supervisor</option>
          <option value="OPD">Operador de donantes</option>
          <option value="OPS">Operador de solicitudes</option>
          <option value="PIN">Personal de inmunología</option>
          <option value="CHO">Coordinador hospitalario</option>
          <option value="OPSR">Operador de solicitudes (Renal)</option>
          <option value="OPSH">Operador de solicitudes (Hepático)</option>
          <option value="OPSC">Operador de solicitudes (Córnea)</option>
          <option value="OPSM">Operador de solicitudes (Médula ósea)</option>
          <option value="OPSV">Operador de solicitudes (Válvulas cardíacas)</option>
          <option value="OPSCOR">Operador de solicitudes (Corazón)</option>
          <option value="OPSP">Operador de solicitudes (Páncreas)</option>
          <option value="OPSPU">Operador de solicitudes (Pulmón)</option>
          <option value="USR">Usuario</option>
        </select>
      </div>

      <div class="mb-3">
        <label class="form-label">Contraseña</label>
        <input
          v-model="form.password"
          type="password"
          class="form-control"
          required
        >
      </div>

      <div class="d-flex justify-content-end gap-2">
        <button type="submit" class="btn btn-primary">
          Guardar
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
// Inicializa el acceso a la variable de entorno para la URL base del backend.
const config = useRuntimeConfig()
// Ahora 'apiBase' contiene la URL base de la API configurada en el .env
const apiBase = config.public.apiBase

// Llamamos al estado global del loader para mostrar el spinner durante la petición
const loader = useState('loader')

// Configuramos el título de la página
useHead({
  title: 'Registrar Usuario',
})

// Campos del formulario para crear un nuevo usuario.
const form = ref({
  username: '',
  email: '',
  first_name: '',
  last_name: '',
  role: '',
  password: ''
})

// Función para guardar el producto
const saveUser = async () => {
  loader.value = true // Activamos el spinner

  // Validación simple para asegurarnos de que los campos no estén vacíos
  try {
    // Usamos $fetch para peticiones manuales (POST, PUT, DELETE)
    await $fetch(`${apiBase}/users/`, {
      method: 'POST',
      body: form.value
    })

    // Si todo sale bien, redirigimos a la lista
    navigateTo('/users')

  } catch (err) {
    console.error('Error saving data:', err)
    console.log('Failed to save user. Check Django logs.')
  } finally {
    loader.value = false // Apagamos el spinner
  }
}
</script>