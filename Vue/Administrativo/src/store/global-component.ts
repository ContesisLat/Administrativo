import { Component } from 'vue';

import ScgParametros from '@/views/Contabilidad/modelos/ScgParametros.vue';
import ScgGpoCtas from '@/views/Contabilidad/modelos/ScgGpoCtas.vue';

 


// Importar todos los componentes globales

// objeto que contiene todos los componentes globales
 
const globalComponents: Record<string, Component> = {
  ScgParametros,
  ScgGpoCtas,

};

  // Agrega todos los demás componentes aquí

export default globalComponents;

