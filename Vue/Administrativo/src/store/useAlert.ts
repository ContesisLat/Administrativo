// src/composables/useAlert.ts
import Swal from 'sweetalert2'

export function useAlert() {
  const success = (message: string, title = 'Éxito') => {
    Swal.fire({
      icon: 'success',
      title,
      text: message,
      confirmButtonText: 'OK'
    })
  }

  const error = (message: string, title = 'Error') => {
    Swal.fire({
      icon: 'error',
      title,
      text: message,
      confirmButtonText: 'OK',
    })
  }

  const warning = (message: string, title = 'Información') => {
    Swal.fire({
      icon: 'warning',
      title,
      text: message,
      confirmButtonText: 'OK'
    })
  }

  const question = (message: string, title = 'Confirmación') => {
    return Swal.fire({
      icon: 'question',
      title,
      text: message,
      showCancelButton: true,
      confirmButtonText: 'Aceptar',
      cancelButtonText: 'Cancelar'
    })
  }

  return {
    success,
    error,
    question,
    warning
  }
}
