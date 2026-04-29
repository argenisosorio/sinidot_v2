// Exportamos funciones individuales
export const utils = () => {
  /* Función para formatear fechas a formato dd/mm/yyyy.
  * Si no hay fecha, devuelve vacío.
  * Convierte 2026-04-20T17:22:20.403Z a 20/04/2026.
  */
  const formatDate = (dateString) => {
    if (!dateString) return ''
    const date = new Date(dateString)
    return new Intl.DateTimeFormat('es-ES', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric'
    }).format(date)
  }

  // Tu función de sumar
  const sumar = (a, b) => {
    return a + b
  }

  return {
    formatDate,
    sumar
  }
}
