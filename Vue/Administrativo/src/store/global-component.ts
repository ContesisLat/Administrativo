import { Component } from 'vue';

import Scgparametros from '@/views/Contabilidad/modelos/ScgParametros.vue';
import ScgGpoCtas from '@/views/Contabilidad/modelos/ScgGpoCtas.vue';

 


// Importar todos los componentes globales

// objeto que contiene todos los componentes globales
 
const globalComponents: Record<string, Component> = {
  Scgparametros,
  ScgGpoCtas

};

  // Agrega todos los demás componentes aquí

export default globalComponents;

