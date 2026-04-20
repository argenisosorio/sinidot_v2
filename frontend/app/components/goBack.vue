<script setup>
// Usamos el router de Nuxt para acceder al historial de navegación
const router = useRouter()

const goBack = () => {
  // .back() funciona exactamente como el botón "atrás" del navegador
  router.back()
}
</script>

<template>
  <button class="btn-back" @click="goBack">
    ⬅ Go back
  </button>
</template>

<style scoped>
</style>
