<template>

  <body>
    <div class="Card">
      <section class="layout">
        <div class="header">
          <div class="row">
            <div class="col">
              <div class="btn-group">
                <button class="btn-insert" @click="startInsert" :disabled="isSearching || isEditing || isDeleting">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-upload" viewBox="0 0 16 16">
                    <path
                      d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5" />
                    <path
                      d="M7.646 1.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 2.707V11.5a.5.5 0 0 1-1 0V2.707L5.354 4.854a.5.5 0 1 1-.708-.708z" />
                  </svg>
                </button>
                <button class="btn-search" @click="startSearch" :disabled="isInserting || isEditing || isDeleting">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-search" viewBox="0 0 16 16">
                    <path
                      d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0" />
                  </svg>
                </button>
                <button class="btn-update" @click="startUpdate" :disabled="!canNavigate">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-pencil-square" viewBox="0 0 16 16">
                    <path
                      d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
                    <path fill-rule="evenodd"
                      d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z" />
                  </svg>
                </button>
                <button class="btn-delete" @click="starDelete" :disabled="!canNavigate">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-trash3" viewBox="0 0 16 16">
                    <path
                      d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5M11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47M8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5" />
                  </svg>
                </button>
              </div>
            </div>
            <div class="col">
              <div class="btn-group">
                <button class="btn-next" @click="goToNext" :disabled="!canNavigate">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-caret-right-fill" viewBox="0 0 16 16">
                    <path
                      d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z" />
                  </svg>
                </button>
                <button class="btn-prev" @click="goToPrev" :disabled="!canNavigate">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-rewind-fill" viewBox="0 0 16 16">
                    <path
                      d="M8.404 7.304a.802.802 0 0 0 0 1.392l6.363 3.692c.52.302 1.233-.043 1.233-.696V4.308c0-.653-.713-.998-1.233-.696z" />
                    <path
                      d="M.404 7.304a.802.802 0 0 0 0 1.392l6.363 3.692c.52.302 1.233-.043 1.233-.696V4.308c0-.653-.713-.998-1.233-.696z" />
                  </svg>
                </button>
                <button class="btn-skipstar" @click="goToFirst" :disabled="!canNavigate">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-skip-start-fill" viewBox="0 0 16 16">
                    <path
                      d="M4 4a.5.5 0 0 1 1 0v3.248l6.267-3.636c.54-.313 1.232.066 1.232.696v7.384c0 .63-.692 1.01-1.232.697L5 8.753V12a.5.5 0 0 1-1 0z" />
                  </svg>
                </button>
                <button class="btn-skipend" @click="goToLast" :disabled="!canNavigate">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-skip-end-fill" viewBox="0 0 16 16">
                    <path
                      d="M12.5 4a.5.5 0 0 0-1 0v3.248L5.233 3.612C4.693 3.3 4 3.678 4 4.308v7.384c0 .63.692 1.01 1.233.697L11.5 8.753V12a.5.5 0 0 0 1 0z" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
        <div class="container">
          <div class="row" style="gap: 20px;">
            <div class="col-10 d-flex flex-column justify-content-center align-items-center" style="gap: 50px;">
              <div class="row">
                <form>
                  <h3><strong>Servicios a Aeronaves</strong></h3>
                  <div class="row mb-1"> <!--Fecha-->
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Fecha</label>
                    <div class="col-sm-3">
                      <input class="form-control form-control-sm" type="date" v-model="formData.fecha"
                        :readonly="onlyRead">
                    </div>
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Estado</label>
                    <div class="col-sm-3">
                      <select class="form-select form-select-sm" v-model="formData.status" :disabled="onlyRead">
                        <option selected>{{ formData.nom_status }}</option>
                        <option value="R" selected>Registrado</option>
                        <option value="F">Facturado</option>
                        <option value="C">Cerrado</option>
                        <option value="A">Anulado</option>
                      </select>
                    </div>
                  </div>
                  <div class="row mb-1"> <!-- Compañía-->
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Compañía</label>
                    <div class="col-sm-3"> <!--Tipo Aeronave-->
                      <select class="form-select form-select-sm" v-model="formData.compania" :disabled="onlyRead">
                        <option selected>{{ descripcionCompania }}</option>
                        <option v-for="i in companias" :key="i.compania" :value="i.compania">{{ i.nombre }}</option>
                      </select>
                    </div>
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Matricula</label>
                    <div class="col-sm-3">
                      <input type="text" class="form-control form-control-sm" v-model="formData.matricula"
                        :readonly="onlyRead">
                    </div>
                  </div>
                  <div class="row mb-1"> <!--Tipo Aeronave-->
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Tipo aeronave</label>
                    <div class="col-sm-3">
                      <select class="form-select form-select-sm" v-model="formData.aeronave" :disabled="onlyRead">
                        <option selected>{{ descripcionAeronaves}}</option>
                        <option v-for="i in aeronaves" :key="i.aeronave" :value="i.aeronave">{{ i.descripcion }}</option>
                      </select>
                    </div>
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Llegada</label>           
                    <div class="col-sm-3">
                      <input class="form-control form-control-sm" type="date" v-model="formData.fecha_llegada"
                        :readonly="onlyRead">
                    </div>
                    <div class="col-sm-3"> 
                      <input class="form-control form-control-sm" type="time" v-model="formData.hora_llegada"
                        :readonly="onlyRead">
                    </div>
                  </div>
                  <div class="row mb-1"> <!--Monto-->
                      <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Monto</label>
                      <div class="col-sm-3">
                        <input type="text" class="form-control form-control-sm" v-model="formData.monto_servicio"
                          :readonly="onlyRead" disabled>
                      </div>
                      <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">No. Factura</label>
                      <div class="col-sm-3">
                        <input type="text" class="form-control form-control-sm" v-model="formData.factura"
                          :readonly="onlyRead" disabled>
                      </div>
                  </div>
                </form>
              </div>
              <div class="row">
                <div class="div-dotted">
                  <form>
                    <div class="row g-3 mb-2" v-for="(registro, index) in registros" :key="index">
                      <!--  Inicio de Agregar Tabla-->

                      <!--  Final de Agregar Tabla-->
                      <div class="col-md-3">
                        <select class="form-select form-select-sm" v-model="registro.cargo" :disabled="tonlyRead">
                          <option selected>{{ descripcionCargos(idncargo)}}</option>
                          <option v-for="i in cargos" :key="i.cargo"  :value="i.cargo" @click="idN(i.cargo)">{{ i.nombre }}</option>
                        </select>
                      </div>
                      <div class="col-md-3">
                        <input v-model="registro.tiempo_total" type="text" v-on:blur="Calcular(index)"   class="form-control form-control-sm"
                          id="validationDefault03" placeholder="Tiempo" :readonly="tonlyRead" >
                      </div>
                      <div class="col-md-3">
                        <input v-model="registro.monto" type="text" class="form-control form-control-sm"
                          id="validationDefault03" placeholder="Monto" disabled >
                      </div>                     
                      <div class="col-sm-3">
                        <select class="form-select form-select-sm" v-model="formData.status" :disabled="tonlyRead">
                          <option selected>{{ registro.nom_status }}</option>
                          <option value="R" selected>Registrado</option>
                          <option value="A">Anulado</option>
                        </select>
                      </div> 
                    </div>
                  </form>
                </div>
              </div>
            </div>
            <div class="col"
              style=" background-color:rgba(255, 255, 255, 0.3);  backdrop-filter: blur(10px); border-radius: 10px;">
              <div class="btn-group2">
                <button type="button" class="btn btn-light btn-sm" @click="toggleSearch" :disabled="!canUseGroup2">{{
                  ButtonText }}</button>
                <button type="button" class="btn btn-light btn-sm" @click="resetAll" :disabled="!canUseGroup2">{{
                  ButtonText2 }}</button>
                <ExRegSerAero v-if="print" :fecha="formData.fecha" :compania="formData.compania" :matricula="formData.matricula" 
                  :aeronave="formData.aeronave" :fecha_llegada="formData.fecha_llegada" :hora_llegada="formData.hora_llegada" :status="formData.status" :tabla="registros"/>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </body>
</template>

<script lang="ts" setup>
import { ref, watch, computed,onMounted } from 'vue'
import axios from 'axios';
import { useAlert } from '@/store/useAlert';
const { success, error, question, warning } = useAlert()
import { UrlGlobal } from '@/store/dominioGlobal';
import { userGlobalStore } from '@/store/userGlobal';
import { useDateTimeStore } from '@/store/dateTimeStore';
import ScgGpoCtas from './ScgGpoCtas.vue';
 
 

const dUrl = UrlGlobal()
const userStore = userGlobalStore()
const dateTimeStore = useDateTimeStore();

function Calcular(indx: any) : void {
  console.log('calculando')
  let id_aeronave = formData.value.aeronave
  let id_fecha = formData.value.fecha
  let id_cargo = registros.value[indx].cargo
  let tiempow = registros.value[indx].tiempo_total

   
  const patronHora = /^([0-9]{1,2}):([0-5][0-9])$/
  if (!patronHora.test(tiempow)) {
    error ('Dato no cumple con el formato hora')
    return
  }
  
  if (tiempow !== '00:00') { 
    axios.get( dUrl.urlGlobal + `/api2/cartarvue/tarifas?id_aeronave=${id_aeronave}&id_fecha=${id_fecha}&id_cargo=${id_cargo}
        &id_tiempo=${tiempow}`)
        .then(response => {
      dataList.value = response.data
      let cartarvue = dataList.value

      registros.value[indx].monto = cartarvue[0].costo_hora

      let montoServicio = 0
      console.log(registros.value.length)
      for (let i = 0; i < registros.value.length; i++) {
        console.log(i)
        console.log(registros.value[i].monto)

        let montoLinea = parseFloat(registros.value[i].monto)
        console.log(montoLinea)

        if (registros.value[i].cargo) {
          montoServicio += montoLinea
          console.log(montoServicio)
        }         
      }
      formData.value.monto_servicio = montoServicio
      })
    }
  }
//--------------------------------------------------------------------------------------------------------------
type Registro = {
  cargo: string
  tiempo_total: string // | null
  monto: string
  status: string
  nom_status: string
}
// Inicializa con una sola fila vacía
const registros = ref<Registro[]>([
  { cargo: '', tiempo_total: '', monto: '0', status: 'R', nom_status:'Registrado'}
])

//const cartarvue = ref<Cartarvue[]>([
//  { costo_hora: '' }
//])
// Estado del formulario y la data
const formData = ref({
  fecha: '',
  compania: '',
  matricula: '',
  aeronave: '',
  fecha_llegada: '',
  hora_llegada: '',
  monto_servicio: 0,
  factura: '',
  status: '', 
  nom_status: ''  
});

// Variables de control
const dataList = ref<any[]>([]); // Lista de datos de la API
const currentIndex = ref(0);
const isEditing = ref(false);
const isSearching = ref(false);
const isInserting = ref(false);
const isDeleting = ref(false)
const print = ref(false)
const canNavigate = ref(false);
const onlyRead = ref(true);
const tonlyRead = ref(true);
const ButtonText = ref('OK')
const ButtonText2 = ref('Cancelar')

// Deshabilita los botones de btn-group2 si no está en modo búsqueda o insercion
const canUseGroup2 = computed(() => isSearching.value || isInserting.value || isEditing.value || isDeleting.value);

//------------------------------------------------------------------------------------------------------------------

//Funciones---------------------------------------------------------------------------------------------------------
// Función para iniciar inserción
const startInsert = () => {
  isInserting.value = true;
  isSearching.value = false;
  isEditing.value = false;
  isDeleting.value = false;
  onlyRead.value = false;
  tonlyRead.value = false
  ButtonText.value = 'Insertar';
  formData.value.status = 'R'
  formData.value.nom_status = 'Registrado'
};

// Función para iniciar búsqueda
const startSearch = () => {
  isSearching.value = true;
  isInserting.value = false;
  isEditing.value = false;
  isDeleting.value = false;
  onlyRead.value = false;
  print.value = false;
};

// Funcion para iniciar edición
let pk: string
const startUpdate = () => {
  isEditing.value = true;
  isInserting.value = false;
  isSearching.value = false;
  isDeleting.value = false;
  canNavigate.value = false;
  onlyRead.value = false;
  tonlyRead.value = false;
  ButtonText.value = 'Editar';
  ButtonText2.value = 'Volver';
  pk = formData.value.fecha, formData.value.compania, formData.value.matricula
};

//funcion para iniciar eliminacion
const starDelete = () => {
  isDeleting.value = true;
  isEditing.value = false;
  isInserting.value = false;
  isSearching.value = false;
  canNavigate.value = false;
  onlyRead.value = true;
  ButtonText.value = 'Eliminar';
  ButtonText2.value = 'Volver'
};

// Función para hacer la consulta
const handleSearch = async () => {
  try {
    const response = await axios.post(dUrl.urlGlobal + '/api2/query', { tabla: 'caratvue', filtro: formData.value });
    dataList.value = response.data;
    currentIndex.value = 0;
    updateFormData();

    if (dataList.value.length === 0) {
      warning('No se ha encontrado registros con los datos ingresados', 'Vuelva hacer la consulta')
      ButtonText.value = 'Ok';
    } else {
      ButtonText.value = 'Consulta';
      canNavigate.value = true;
      print.value = true;
      onlyRead.value = true;
      getCaratvue()
    }
  } catch (err: any) {
    error(err.response?.data?.detail || 'Ocurrió un error en la consulta.')
  }
};

// Valida Array
function valida(arr: string[]): boolean {
  let valido = true
  const uniqueElement = new Set(arr)
  if (arr.length != uniqueElement.size) {
    valido = false
  }

  return valido
}
//Funcion para la insercion
const handleInsert = async () => {
  let vali = 0
  // Mostrar confirmación
  if (!formData.value.fecha) {
    error('Digite la fecha del Servicio...')
    return
  }
  if(!formData.value.compania){
    error('Digite la compañía aerea...')
    return
  }
  if (!formData.value.aeronave) {
    error('Escoja el tipo de aeronave...')
    return
  }
  if (!formData.value.matricula) {
    error('Digite el número de la matrícula...')
    return
  }
  if(!formData.value.fecha_llegada || !formData.value.hora_llegada) {
    error('Digite la fecha y hora de llegada de la aeronave...')
    return
  }
  if (formData.value.fecha_llegada > formData.value.fecha) {
    error('Fecha del servicio no puede ser menor a la fecha de llegada de la aeronave...')
    return
  }

  // VALIDAR ARREGLO
  let lineas = registros.value.length
  
  if (!registros.value) {
    error('Digite los detalles del servicio')
    return
  }
   
  const guiaArray: string[] = registros.value.map(item => item.cargo)

  let resultado: boolean = valida(guiaArray);

  if (!resultado) {
    error('Existen Cargos repetidos, verifique... ')
    return
  }

  let montoServicio = 0
  const patronHora = /^([0-9]{1,2}):([0-5][0-9])$/
  
  for (let i = 0; i < registros.value.length -1; i++) {
    const arreglo = registros.value[i]
    if (i != lineas) {
      if (!arreglo.cargo) {
        error('Hay codigos de cargos que no se han registrado...')
        return
      }
      const valor = parseFloat(arreglo.monto)
      if ( valor < 1 || typeof valor != 'number' ) {
        error( `Monto en la posicion ${i + 1}, es incorrecto...`)
        return
      }
    }
  }
  const result = await question(
    'Se va a insertar el campo con los nuevos datos.',
    '¿Deseas insertar este registro?'
  )

  if (!result.isConfirmed) {
    // Usuario canceló, salimos de la función
    return
  }

  const data = {
    model: "caratvue",
    data: {
      fecha: formData.value.fecha,
      compania: formData.value.compania,
      matricula: formData.value.matricula,
      aeronave: formData.value.aeronave,
      fecha_llegada: formData.value.fecha_llegada,
      hora_llegada: formData.value.hora_llegada,
      creado_por: userStore.globalUser,
      fecha_creado: dateTimeStore.formattedDate,
      hora_creado: dateTimeStore.formattedTime,
      monto_servicio: formData.value.monto_servicio,
      status: formData.value.status,
    }
  }
  try {
    const response = await fetch(dUrl.urlGlobal + '/api2/insert/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })

    if (!response.ok) {
      error('Ocurrió un error al insertar los datos.', 'Formulario')
    }
    else {
      vali++
      for (const fila of registros.value) {
        if (fila.cargo == "" || fila.cargo == undefined) {
          vali++
          break
        }
        const data = {
        model: "caratvued",
        data: {
          fecha: formData.value.fecha,
          compania: formData.value.compania,
          matricula: formData.value.matricula,
          creado_por: userStore.globalUser,
          fecha_creado: dateTimeStore.formattedDate,
          hora_creado: dateTimeStore.formattedTime, 
          cargo: fila.cargo,
          tiempo_total: fila.tiempo_total,
          monto: fila.monto, 
          status: formData.value.status
        }
      }
      try {
        const response = await fetch(dUrl.urlGlobal + '/api2/insert/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
        })

        if (!response.ok) {
          // Puedes registrar el error y seguir con el siguiente
          console.log(`Error al insertar registro con cargo: ${fila.cargo}`)
        }else{
          vali++
        }
      } catch (err: any) {
        error(`Error inesperado el cargo ${fila.cargo}:`, err)
      }
    }
    }
    } catch (err: any) {
      error(err.response?.data?.detail || 'Ocurrió un error al insertar los datos.')
      }

  if (vali > registros.value.length) {
    success('Los datos fueron insertados correctamente.', 'Insercion multiple exitosa')
  }
}

//funcion para el update
const handleUpdate = async () => {
  // Mostrar confirmación
  const result = await question(
    'Se va a actualizar el campo con los nuevos datos.',
    '¿Deseas actualizar este registro?'
  )

  if (!result.isConfirmed) {
    // Usuario canceló, salimos de la función
    return
  }

  try {
    const response = await axios.post(dUrl.urlGlobal + '/api2/update/', {
      table: 'caratvue',
      filters: { fecha: formData.value.fecha, compania: formData.value.compania, matricula: formData.value.matricula }, // Filtro para identificar el registro a actualizar
      data: {
        fecha_llegada: formData.value.fecha_llegada,
        hora_llegada: formData.value.hora_llegada,
        monto_servicio: formData.value.monto_servicio,
        aeronave: formData.value.aeronave,
        status: formData.value.status,
        modificado_por: userStore.globalUser,
        fecha_status: dateTimeStore.formattedDate,
        hora_status: dateTimeStore.formattedTime
      } // Datos a actualizar
    })
    if (response.status == 200) {
// Update del detalle
      for (const fila of registros.value) {
        if (fila.cargo == "" || fila.cargo == undefined) {
          break
        }
        
        const response = await axios.post(dUrl.urlGlobal + '/api2/query', { 
          tabla: 'caratvued', 
          filtro: { fecha: formData.value.fecha, compania: formData.value.compania, 
                    matricula: formData.value.matricula, cargo: fila.cargo }});
                    
        dataList.value = response.data;
        if (dataList.value.length == 0) {
          const data = {
            tabla: 'caratvued',
            data: {
              fecha: formData.value.fecha,
              compania: formData.value.compania,
              matricula: formData.value.matricula,
              cargo: fila.cargo,
              creado_por: userStore.globalUser,
              fecha_creado: dateTimeStore.formattedDate,
              hora_creado: dateTimeStore.formattedTime,
              tiempo_total: fila.tiempo_total,
              monto: fila.monto,
              status: fila.status
            }
          }
          try {
            const response = await fetch( dUrl.urlGlobal + '/api2/insert/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify(data),
            })

            if (!response.ok) {
              error(`Error insertando el cargo ${fila.cargo}`)
            }else {
              try {
                const response = await axios.post( dUrl.urlGlobal + '/api2/update/', {
                  table: 'caratvued',
                  filters: { fecha: formData.value.fecha, compania: formData.value.compania,
                            matricula: formData.value.matricula, cargo: fila.cargo },
                  data: {
                    cargo: fila.cargo,
                    tiempo_total: fila.tiempo_total,
                    monto: fila.monto,
                    modificado_por: userStore.globalUser,
                    fecha_status: dateTimeStore.formattedDate,
                    hora_status: dateTimeStore.formattedTime
                  }
                })
                if (response.status != 200) {
                  error(`Error actualizando el cargo ${fila.cargo}`)
                }
              } 
              catch (err: any) {
                error(err.response?.data?.detail || `Error actualizando el cargo ${fila.cargo}`)
              }
            }
          } catch (err: any) {
            error(err.response?.data?.detail || `Error Insertando el cargo ${fila.cargo}`)
          }
        } 
      } 
// Fin del Update del detalle
      success('Los datos fueron actualizados correctamente.', 'Actualización exitosa')

    } else {
      error('Ocurrió un error al actualizar los datos.')
    }
  } catch (err: any) {
    error(err.response?.data?.detail || 'Ocurrió un error al actualizar los datos.')
  }
}

//funcion para eliminar
const handleDelete = async () => {
 // Mostrar confirmación
  const result = await question(
    'Se va inactivar el registro.',
    '¿Deseas inhabilitar a este registro?'
  )

  if (!result.isConfirmed) {
    // Usuario canceló, salimos de la función
    return
  }

  try {
    const response = await axios.post(dUrl.urlGlobal + '/api2/update/', {
      table: 'caratvue',
      filters: { fecha: formData.value.fecha, compania: formData.value.compania, matricula: formData.value.matricula }, // Filtro para identificar el registro a actualizar
      data: {
        status: 'I',
      }
    })
    if (response.status == 200) {
      success('el registro fue inhabilitado correctamente.', 'Accion exitosa')
    } else {
      error('Ocurrió un error al inactivar el registro.')
    }
  } catch (err: any) {
    error(err.response?.data?.detail || 'Ocurrió un error inesperado.')
  }
}

// Actualiza el formulario con el registro actual
const updateFormData = () => {
  if (dataList.value.length > 0) {
    formData.value = { ...dataList.value[currentIndex.value] };
  }
};
     
//carga de la tabla
const getCaratvued = ref<any[]>([]);
const getCaratvue = () => {
  getCaratvued.value = []
  registros.value = []
  axios.get(dUrl.urlGlobal + `/api2/caratvued/filter?fecha=${formData.value.fecha}&compania=${formData.value.compania}&matricula=${formData.value.matricula}`)
    .then(response => {
      getCaratvued.value = response.data;
      registros.value = getCaratvued.value.map((i: any) => ({
        cargo: i.cargo || '',
        tiempo_total: i.tiempo_total || '',
        monto: i.monto || null,
        status: i.status || '',
        nom_status: i.nom_status
      }))
    })
    .catch(error => {
      console.error('Error fetching cargos:', error);
    });
};

//carga de las ayudas
const aeronaves = ref<any[]>([]);
const companias = ref<any[]>([]);
const cargos = ref<any[]>([]);
onMounted(async () => {
  const responseA = await axios.get(dUrl.urlGlobal + '/api2/cartiaero/')
  aeronaves.value = responseA.data
  const responseP = await axios.get(dUrl.urlGlobal + `/api2/compania/filter?status=A`)
  companias.value = responseP.data
  const responseN = await axios.get(dUrl.urlGlobal + '/api2/caratenvue/filter?status=A')
  cargos.value = responseN.data
})

//computados de las ayudas
const descripcionAeronaves = computed(() => {
  const encontrado = aeronaves.value.find(i => i.aeronave === formData.value.aeronave)
  return encontrado ? encontrado.descripcion : ''
})

const descripcionCompania = computed(() => {
  const encontrado = companias.value.find(i => i.compania === formData.value.compania)
  return encontrado ? encontrado.nombre : ''
})

const descripcionCargos = (cargosId: string) => {
  const encontrado = cargos.value.find(i => i.cargo === cargosId)
  return encontrado ? encontrado.nombre : ''
}

let idncargo : any
const idN = (naturalezaId: string) => {
  idncargo = naturalezaId
}
//const descripcionNaturaleza = computed(() => {
//  const encontrado = naturaleza.value.find(i => i.naturaleza === registros.value.)
//  return encontrado ? encontrado.nombre
//})
//------------------------------------------------------------------------------------------------------------------

// Navegación entre registros---------------------------------------------------------------------------------------
const goToFirst = () => {
  currentIndex.value = 0;
  updateFormData();
  getCaratvue()
};
const goToPrev = () => {
  if (currentIndex.value > 0) {
    currentIndex.value--;
    updateFormData();
    getCaratvue()
  }
};
const goToNext = () => {
  if (currentIndex.value < dataList.value.length - 1) {
    currentIndex.value++;
    updateFormData();
    getCaratvue()
  }
};
const goToLast = () => {
  currentIndex.value = dataList.value.length - 1;
  updateFormData();
  getCaratvue()
};
//------------------------------------------------------------------------------------------------------------------

// Control de botones submit y cancelar-----------------------------------------------------------------------------------------------

//boton principal que controla el submit
const toggleSearch = () => {
  if (dataList.value.length && isSearching.value == true) {
    // Si ya hay datos, "Consulta" limpia y reinicia la búsqueda
    dataList.value = [];
    formData.value = { fecha: '', compania: '', matricula: '', fecha_llegada: '', hora_llegada: '', monto_servicio: 0, status: '', nom_status: '', factura: '', aeronave: '' };
    onlyRead.value = false;
    ButtonText.value = 'Ok'
    canNavigate.value = false;
    registros.value = []
  } else if (isInserting.value == true) {
    handleInsert();
  } else if (isEditing.value == true) {
    handleUpdate();
  } else if (isDeleting.value == true) {
    handleDelete()
  }
  else {
    // Si no hay datos, hace la consulta
    handleSearch();
  }
};


// Boton que restablece todo a estado inicial
const resetAll = () => {
  if (ButtonText2.value == 'Cancelar') {
    dataList.value = [];
    formData.value = { fecha: '', compania: '', matricula: '', fecha_llegada: '', hora_llegada: '', monto_servicio: 0, factura: '', status: '', nom_status: '', aeronave: '', };
    isInserting.value = false;
    isSearching.value = false;
    isEditing.value = false;
    isDeleting.value = false;
    canNavigate.value = false;
    onlyRead.value = true;
    tonlyRead.value = true;
    ButtonText.value = 'Ok'
    registros.value = []
  } else {
    dataList.value = [];
    formData.value = { fecha: '', compania: '', matricula: '', fecha_llegada: '', hora_llegada: '', monto_servicio: 0, factura: '', status: '', nom_status: '', aeronave: '', };
    startSearch()
    ButtonText.value = 'Ok'
    ButtonText2.value = 'Cancelar'
    registros.value = []
  }

};
//---------------------------------------------------------------------------------------------------------------------------------------------------------


//control de filas automaticas de la tabla-----------------------------------------------------------------------------------------------------------------

// Función para validar si una fila está completamente llena
const filaLlena = (fila: Registro | undefined | null) => {
  if (!fila) return false;

  return Object.values(fila).every(val => {
    if (typeof val === 'string') {
      return val.trim() !== ''
    }
    if (typeof val === 'number') {
      return !isNaN(val)
    }
    return false
  })
}

// Observar el último elemento y agregar uno nuevo si está lleno
watch(registros, (newVal) => {
  // Evitar errores si el array está vacío
  if (!newVal.length) {
    registros.value.push({
      cargo: '',
      tiempo_total: '',
      monto: '0',
      status: '',
      nom_status: ''
    });
    return;
  }

  // Evaluar la última fila
  const ultimaFila = newVal[newVal.length - 1];
  if (filaLlena(ultimaFila)) {
    registros.value.push({
      cargo: '',
      tiempo_total: '',
      monto: '0',
      status: 'R',
      nom_status: 'Registrado'
    });
  }
}, { deep: true });
//-----------------------------------------------------------------------------------------------------------------------------------------------------------
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

body {
  height: 100%;
  width: 100%;
  background: transparent;
  backdrop-filter: blur(10px);
}

.Card {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 95%;
  height: 95%;
  display: flex;
  border-radius: 10px;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  text-align: center;
  font-family: 'Poppins', sans-serif;
  color: white;
  background: linear-gradient(to right, #ccd0cf, #9ba8ab, #4a5c6a);
  overflow: hidden;

  @media screen and (max-width: 600px) {
    overflow: scroll;
  }
}

.layout {
  position: absolute;
  width: 95%;
  height: 95%;

  display: grid;
  grid:
    "header" auto "container" 1fr / 1fr;
  gap: 50px;
}

.header {
  display: flex;
  justify-content: left;
  align-items: left;
  grid-area: header;
}

.container {
  grid-area: container;
}

.btn-group {
  display: flex;
  justify-content: flex-end;
  gap: 20px;
  margin-top: 20px;
  padding: 5px;
  background-color: rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(10px);
  border: none;
  border-radius: 10px;
}

.btn-group button {
  border: none;
  border-radius: 20px;
  background-color: transparent;
  transition: transform 0.2s ease;
}

.btn-group button:active {
  transform: scale(0.95);
}

.btn-group button:hover {
  background: #001982;
  color: white;
}

.btn-group2 {
  display: flex;
  justify-content: center;
  flex-direction: column;
  gap: 20px;
  margin-top: 20px;
  padding: 5px;
  border: none;
  border-radius: 10px;
}

.btn-group2 button {
  transition: transform 0.2s ease;
  overflow: hidden;
}

.btn-group2 button:active {
  transform: scale(0.95);
}

.div-dotted {
  height: 150px;
  position: relative;
  border: 1px dotted whitesmoke;
  display: flex;
  padding: 20px;
  overflow-y: scroll;
}
</style>