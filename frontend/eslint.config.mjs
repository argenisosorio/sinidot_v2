// eslint.config.mjs
import withNuxt from './.nuxt/eslint.config.mjs'

export default withNuxt({
  // Aquí puedes agregar reglas personalizadas si quieres
  rules: {
    'vue/multi-word-component-names': 'off', // Para que no se queje de nombres como "Navbar"
  }
})