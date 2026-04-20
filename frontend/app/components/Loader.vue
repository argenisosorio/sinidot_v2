<template>
  <div class="loader-overlay">
    <div class="spinner" />
  </div>
</template>

<style scoped>
/* 1. El fondo que cubre toda la pantalla */
.loader-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.7); /* Oscurecemos el fondo */
  display: flex;
  justify-content: center; /* Centra horizontalmente */
  align-items: center;     /* Centra verticalmente */
  z-index: 10000;
  backdrop-filter: blur(4px); /* Efecto desenfoque moderno */
}

/* 2. El círculo animado */
.spinner {
  width: 60px;
  height: 60px;
  border: 6px solid rgba(255, 255, 255, 0.1); /* Círculo de fondo tenue */
  border-left-color: #0011ff; /* El color morado que pediste */
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

/* Animación de rotación */
@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>