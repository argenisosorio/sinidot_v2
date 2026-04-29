// Exportamos funciones individuales
export const utils = () => {
  /**
   * Función para formatear fechas a formato dd/mm/yyyy.
   * Si no hay fecha, devuelve vacío.
   * Convierte 2026-04-20T17:22:20.403Z a 20/04/2026.
   *
   * @param dateString - La fecha a formatear.
   *
   * @returns La fecha formateada o vacío si no hay fecha.
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

  /**
   * Método que asigna un valor a la variable roleType dependiendo del
   * valor de la variable role para así mostrar el valor asignado en
   * la tabla de registros.
   *
   * @param role - El rol del usuario, representado por un código específico
   * (por ejemplo, "ADM" para Administrador).
   *
   * @returns El nombre completo del rol correspondiente al código
   * proporcionado. Si el código no coincide con ninguno de los casos definidos,
   * devuelve una cadena vacía.
   */
  const showRole = (role) => {
      let roleType = "";
      if (role === "ADM") {
        roleType = "Administrador";
      }
      else if (role === "SUP") {
        roleType = "Supervisor";
      }
      else if (role === "OPD") {
        roleType = "Operador de donantes";
      }
      else if (role === "OPS") {
        roleType = "Operador de solicitudes";
      }
      else if (role === "OPSR") {
        roleType = "Operador de solicitudes (Renal)";
      }
      else if (role === "OPSH") {
        roleType = "Operador de solicitudes (Hepático)";
      }
      else if (role === "OPSC") {
        roleType = "Operador de solicitudes (Córnea)";
      }
      else if (role === "OPSM") {
        roleType = "Operador de solicitudes (Médula ósea)";
      }
      else if (role === "OPSV") {
        roleType = "Operador de solicitudes (Válvulas cardíacas)";
      }
      else if (role === "OPSCOR") {
        roleType = "Operador de solicitudes (Corazón)";
      }
      else if (role === "OPSP") {
        roleType = "Operador de solicitudes (Páncreas)";
      }
      else if (role === "OPSPU") {
        roleType = "Operador de solicitudes (Pulmón)";
      }
      else if (role === "PIN") {
        roleType = "Personal de inmunología";
      }
      else if (role === "CHO") {
        roleType = "Coordinador hospitalario";
      }
      else if (role === "USR") {
        roleType = "Usuario";
      }
      return roleType;
  }

  // Retornamos las funciones para que puedan ser utilizadas en otros componentes.
  return {
    formatDate,
    showRole
  }
}
