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
  </div>
</template>

<script setup>
// Protege esta página con el middleware de autenticación.
definePageMeta({
  middleware: ['auth'],
})

// Configura el título de la página.
useHead({
  title: 'SINIDOT - Inicio'
})

const loader = useState('loader')

onMounted(() => {
  console.log("Activo el loader")
  loader.value = true

  setTimeout(() => {
    loader.value = false
    console.log("Ha pasado 1 segundo y quité el loader")
  }, 1000)
})
</script>