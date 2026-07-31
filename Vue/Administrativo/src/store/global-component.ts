import { Component } from 'vue';

import ScgParametros from '@/views/Contabilidad/Generales/ScgParametros.vue';
import ScgGpoCtas from '@/views/Contabilidad/Generales/ScgGpoCtas.vue';
import ScgCatalogo from '@/views/Contabilidad/Generales/ScgCatalogo.vue';
import ScgTerc from '@/views/Contabilidad/Generales/ScgTerc.vue';
import ScgTerceros from '@/views/Contabilidad/Generales/ScgTerceros.vue';
import ScgAfecTransac from '@/views/Contabilidad/AfectacionContable/ScgAfecTransac.vue';
import ScgGerenDept from '@/views/Contabilidad/AfectacionContable/ScgGerenDept.vue';
//import ScgGpoCtas from '@/views/Contabilidad/modelos/ScgGpoCtas.vue';

 

// Importar todos los componentes globales

// objeto que contiene todos los componentes globales
 
const globalComponents: Record<string, Component> = {
  ScgParametros,
  ScgGpoCtas,
  ScgCatalogo,
  ScgTerceros,
  ScgAfecTransac,
  ScgGerenDept

};

  // Agrega todos los demás componentes aquí

export default globalComponents;

