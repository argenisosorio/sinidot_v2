<template>
  <div class="mb-3">
    <!--nav class="navbar navbar-expand-lg border-bottom">
      <div class="container-fluid">
        <div class="navbar-nav flex-row">
          <NuxtLink class="nav-link" to="https://fundavene.gob.ve/">
            FUNDAVENE
          </NuxtLink>
          <NuxtLink class="nav-link" to="/">INICIO</NuxtLink>
          <NuxtLink class="nav-link" to="/users">GESTIÓN DE USUARIOS</NuxtLink>
        </div>
      </div>
    </!nav-->
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
                <li><a class="dropdown-item" href="#">xxxx</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<style scoped>
</style>