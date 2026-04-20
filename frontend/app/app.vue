<template>
  <div>
    <!-- El loader se muestra condicionalmente según el estado global 'loader' -->
    <Loader v-if="loader" />
    <div class="container">
      <Navbar />
      <NuxtPage />
      <Footer />
    </div>
  </div>
</template>

<script setup>
/* Estado global para controlar la visibilidad del loader
 * Inicialmente el loader no está visible
*/
const loader = useState('loader', () => false)
</script>

<style>
</style>
