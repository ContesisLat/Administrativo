<template>
  <body>
    <div class="Card">
      <section class="layout">
          <div class="container">
              <div class="row" style="gap: 5px;">
                <div class="col d-flex flex-column justify-content-center align-item-center" >
                  <h3><strong>Movimientos del Cuarto Frío</strong></h3>
                  <!--FormData-->
                  <div class="row">
                    <form>
                      <div class="row mb-1">
                        <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Fecha Inicio</label>
                        <div class="col-sm-2">
                          <input class="form-control form-control-sm" type="date" v-model="formData.fecha_inicio"
                            :readonly="onlyRead">
                        </div>
                        <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Fecha Final</label>
                        <div class="col-sm-2">
                          <input class="form-control form-control-sm" type="date" v-model="formData.fecha_final"
                            :readonly="onlyRead">
                        </div>
                      </div>
                      <div class="row mb-1">
                        <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Tipo</label>
                        <div class="col-sm-2">
                          <select class="form-select form-select-sm" v-model="formData.tipo" >
                            <option selected>{{ formData.tipo }}</option>
                            <option value="T" selected>Todos</option>
                            <option value="E">Entradas</option>
                            <option value="S">Salidas</option>
                          </select>
                        </div>
                        <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Estado</label>
                        <div class="col-sm-2">
                          <select class="form-select form-select-sm" v-model="formData.status" >
                            <option selected>{{ formData.tipo }}</option>
                            <option value="T" selected>Todas</option>
                            <option value="I">Ingresadas</option>
                            <option value="C">Calculadas</option>
                            <option value="D">Despachadas</option>
                          </select>
                        </div>   
                      </div>
                      <div class="row mb-1">
                        <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Movimiento</label>
                        <div class="col-sm-3">
                          <select class="form-select form-select-sm" v-model="formData.codigo" >
                            <option selected>{{ descripcionCodigo }}</option>
                            <option v-for="op in codigos" :key="op.codigo" :value="op.codigo">{{ op.descripcion }}</option>
                          </select>
                        </div>
                      </div>
                    </form>
                  </div>
                  <!--FormData-->
                  <h3><strong>Control de Movimientos</strong></h3>
                  <div class="card overflow-scroll w-100">
                      <table class="table table-hover  table-sm">
                          <thead>
                              <tr>
                                  <th>Fecha</th>
                                  <th>Cliente</th>
                                  <th>Movimiento</th>
                                  <th>Documento</th>
                                  <th>Guía</th>
                                  <th>Llegada/Salida</th>
                                  <th>Llegada/Salida</th> 
                                  <th>Valor</th>
                                  <th>Estado</th> 
                              </tr>
                          </thead>
                            <tbody>
                              <tr v-for="elm in filteredCarga1" :key="elm.id"
                                  @click="getLogdemo(elm.compania, elm.agencia, elm.fecha, elm.almacen, elm.codigo, elm.documento, elm.id)"
                                    :class="{ 'table-primary': elm.id === id_ref }">
                                  <td>{{ elm.fecha }}</td>
                                  <td>{{ elm.nom_cliente }}</td>
                                  <td>{{ elm.nom_codigo }}</td>
                                  <td>{{ elm.documento }}</td>
                                  <td>{{ elm.guia_despacho }}</td>
                                  <td>{{ elm.fecha_llegada }}</td>
                                  <td>{{ elm.hora_llegada }}</td>
                                  <td>{{ elm.valor }}</td>
                                  <td>{{ elm.nom_status}}</td>
                              </tr>
                            </tbody>
                      </table>  
                  </div>
                  <h3><strong>Detalles de Movimientos</strong></h3>
                  <div class="card overflow-scroll w-100">
                      <table class="table table-hover  table-sm">
                          <thead>
                              <tr>
                                <th>Secuencia</th>
                                <th>Id. Pallet</th>
                                <th>Cant Pallets</th>
                                <th>Cajas/Bultos</th>
                                <th>Peso Kg</th>
                                <th>Monto</th>
                                <th>Estado</th>
                              </tr>
                          </thead>
                          <tbody>
                              <tr v-for="elm1 in logdemo" :key="elm1.secuencia"
                                 @click="true" :class="{ 'table-primary': elm1.id === de_ref }" >
                                <td>{{ elm1.secuencia }}</td>
                                <td>{{ elm1.orden_produccion }}</td>
                                <td>{{ elm1.pallets }}</td>
                                <td>{{ elm1.cajas }}</td>
                                <td>{{ elm1.peso }}</td>
                                <td>{{ elm1.monto }}</td>
                                <td>{{ elm1.nom_status}}</td>
                              </tr>
                          </tbody>
                      </table>
                  </div>
                </div> 
                <div class="col div-buttom"
                      style=" background-color:rgba(255, 255, 255, 0.3);  backdrop-filter: blur(10px); border-radius: 10px; height: 300px;">
                      <div class="btn-group2">
                        <!--button type="button" class="btn btn-light" @click.prevent="Null">Buscar</button-->
                        <button type="button" class="btn btn-light" @click="Entrada">Movimientos</button>
                        <button type="button" class="btn btn-light" @click="Calcular">Calcular</button>
                        <button type="button" class="btn btn-light" @click="Despachar">Entrega</button>
                        <button type="button" class="btn btn-light" @click="Listar">Reporte</button>
                        <button type="button" class="btn btn-light" @click="Auxiliar">Auxiliar</button>
                        <!--button type="button" class="btn btn-light" @click="Anular" :disabled="!canUseGroup2">Anular</button-->
                      </div>
                </div>
              </div>
          </div>
          <InCuartoFrio v-if="btnIn" :fecha="fecha" :btnIn="btnIn" @insertProps="insertPropsValue" />
          <ExCuartoFrio v-if="btnEx" :btnEx="btnEx" @insertProps="ExcelPropsValue" />
      </section>
    </div>
  </body>
</template>

<script lang="ts" setup>
 
import { ref, onMounted, computed, Ref, defineProps, defineEmits } from 'vue';
import axios from 'axios';
import { useAlert } from '@/store/useAlert';
const {success, error, question,warning} = useAlert()
import { UrlGlobal } from '@/store/dominioGlobal';
const dUrl = UrlGlobal()
const search = ref('')
const options = ref('')
import { Logctmo, Logdemo, LogTral } from '@/interface/interfaces';
 
import { flattenDiagnosticMessageText } from 'typescript';
import InCuartoFrio from './pInsert/InCuartoFrio.vue';
import ExCuartoFrio from './pImpresion/ExCuartoFrio.vue';
import { useDateTimeStore } from '@/store/dateTimeStore';


const dateTimeStore = useDateTimeStore()

const id_ref = ref<string | null>(null)
const de_ref = ref<string | null>(null)
const fecha_ctrl = ref<string | null>(null)
//--------------------------------------------------------------------------------------------------------------
const logctmo = ref<Array<Logctmo>>([]);

const getLogctmo = () => { 
        axios.get(dUrl.urlGlobal +'/api2/logctmo/')
            .then(response => {
                logctmo.value = response.data;
              
            //let almacen = response.data.almacen
            //let area = response.data.area

            })
            .catch(error => {
                console.error('Error buscando control de Movimientos:', error);
            });
};
//----------------------------------------------------------------
const logdemo = ref<Array<Logdemo>>([])
const getLogdemo = (id_compania: any, id_agencia: any, id_fecha: any, id_almacen: any, id_codigo: any, id_documento: any, id: any) => {
        id_ref.value = id
        fecha = id_fecha
        codigo = id_codigo
        documento = id_documento
         
        axios.get(`${dUrl.urlGlobal}/api2/logctmo/logdemo?id_compania=${id_compania}&id_agencia=${id_agencia}&id_fecha=${id_fecha}&id_almacen=${id_almacen}&id_codigo=${id_codigo}&id_documento=${id_documento}`)
        //axios.get(final)    
            .then(response => { //console.log(response.data)
                logdemo.value = response.data;
                console.log(response.data)

            })
            .catch(error => {
                console.error('Error buscando detalles de movimientos:', error);
        });
    }
//};

// Estado del formulario y la data
const formData = ref({
  fecha_inicio: '',
  fecha_final: '',
  tipo: '',
  status: '',
  codigo: '',
  nom_codigo: ''

});
//funcion de los botones y las extenciones de Insert,delete,update----------------
let fecha: any
let codigo: any
let documento: any

let btnIn = ref(false);//variable modal insert
let btnEx = ref(false);//variable para mostrar modal de update
let clickEx = ref(false)//variable para activar el click de Up
let btnCoUp = ref(false)
let clickCoUp = ref(false)

//funciones q activan el click y en el caso del insert muestran el modal
const CbtnEx = () => {
  clickEx.value = !clickEx.value
   
}
function insertPropsValue(newValue: boolean) {
  btnIn.value = newValue
  getLogctmo()
  getLogdemo("1", "1", null, "1", "1", "1", "1")
}

function ExcelPropsValue(newValue: boolean) {
  btnEx.value = newValue

  getLogctmo()
  getLogdemo("1", "1", "1", null, "1", "1", "1")
}
//--- Fun//funcion principal para el funcionamiento de el update y delete cuando uno de los 2 este activado
const Auxiliar = async() => {
    if (!id_ref.value) {
      error('Seleccione la línea que generará el auxiliar...')
      return
    }
    try {
        const response = await axios.post(dUrl.urlGlobal + '/api2/query', { tabla: 'logctmo', 
            filtro: { id:id_ref.value }});

        dataList.value = response.data;

    } catch (err: any) {
        error(err.response?.data?.detail || 'Ocurrió un error en la consulta.')
    }
    const envio_data = computed(() => ({
        fecha: dataList.value[0].fecha,
        almacen: '02',
        codigo: dataList.value[0].codigo,
        documento: dataList.value[0].documento, 
        status: dataList.value[0].status 
    }));

    try {
        const response = await axios.post(
        dUrl.urlGlobal + '/api2/AuxLogctmo_excel',
        envio_data.value,
        { responseType: 'blob' }
        );
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'auxiliar_logctmo.xlsx');
        document.body.appendChild(link);
        link.click();
        window.URL.revokeObjectURL(url);
        success('Se generó el Auxiliar del Movimiento', 'Auxiliar en descargas')
    } catch (error) {
        console.error('Error al generar el auxiliar:', error);
      }
}

const Despachar = async() => {
  console.log(id_ref.value)
  if (!id_ref.value) {
    error('Debe seleccionar la guía a entregar')
    return
  }

  for (let i = 0; i < logctmo.value.length; i++) {
    console.log(i)
    if (id_ref.value == logctmo.value[i].id) {
      if (logctmo.value[i].status == "D") {
        error('Este Registro ya fué Despachado... ')
        return
      }
      if (logctmo.value[i].status == "I") {
        error('Ante de Despachar debe realizar el cálculo del servicio... ')
        return
      }
      break;
    }
  }

  const result = await question(
    'Se generará la salida del Cuarto Frío... ',
    '¿Seguro desea continuar?'
  )

  if (!result.isConfirmed) {
    // Usuario canceló, salimos de la función
    return
  }

  axios.get(`${dUrl.urlGlobal}/api2/logctmo/salida?id=${id_ref.value}`) 
    .then(response => {
      console.log("Generado")
      getLogctmo
      getLogdemo("1", "1", null, "1", "1", "1", "1")
    })
    .catch(error => {
      console.log('Error en el Despacho:', error)
    })   

};

  //-- Funciones de Botones
const Calcular = async() => {
  console.log(id_ref.value)

  if(!id_ref.value) {
    error('Debe marcar el movimiento que va a calcular... ')
    return
  }
  
  if (formData.value.status =='D') {
    error('Este movimiento ya fué despachado...')
    return
  }

  try {
      const response = await axios.post(dUrl.urlGlobal + '/api2/query', { tabla: 'logdemo', 
          filtro: { compania:'300', agencia: '001', fecha: fecha, almacen: '02', 
              codigo: codigo, documento: documento }});

      dataList.value = response.data;

      if (dataList.value.length == 0) {
        warning('Ingreso no tiene detalles', 'No se generarán cálculos')
        return
        }

    } catch (err: any) {
        error(err.response?.data?.detail || 'Ocurrió un error en la consulta.')
    }

  const result = await question(
    'Se generarán los calculos con tarifa de Refrigeración... ',
    '¿Seguro desea continuar?'
  )

  if (!result.isConfirmed) {
    return
  }

  axios.get(`${dUrl.urlGlobal}/api2/logctmo/calculo?id=${id_ref.value}`) 
    .then(response => {
      console.log("Generado")
      
      getLogctmo()
      getLogdemo("1", "1", null, "1", "1", "1", "1")
    })
    .catch(error => {
      console.log('Error calculando:', error)
    })
}

const Entrada = () => {   
  btnIn.value = !btnIn.value
  fecha = dateTimeStore.formattedDate
   
}

const Listar = () => {
  btnEx.value = !btnEx.value
  let calcular = false
}

const Anular = () => {
  let calcular = false
}

//-----------------------------------------------------------------
// Filtrar los registros que coincidan con el valor de búsqueda en cualquiera de los campos segun la tabla------------------------------------------------
const filteredCarga1 = computed(() => {
    if (search.value === '') {
        // Si no hay nada en la búsqueda, retornar todos los registros
        return logctmo.value;
    } else if (options.value == 'fecha') {
        // Convertir el término de búsqueda a minúsculas para hacer la búsqueda insensible a mayúsculas
        const searchTerm = search.value.toLowerCase();
        // Filtrar los registros que coincidan con el valor de búsqueda en cualquiera de los campos
        return logctmo.value.filter(elm => {
            return (
                elm.fecha?.toLowerCase().includes(searchTerm) ||
                elm.cliente?.toLocaleLowerCase().includes(searchTerm) ||
                elm.codigo?.toLowerCase().includes(searchTerm) ||
                elm.documento?.toLowerCase().includes(searchTerm) ||
                elm.fecha_llegada?.toLowerCase().includes(searchTerm) ||
                elm.hora_llegada?.toLowerCase().includes(searchTerm) ||
                elm.nom_status?.toLowerCase().includes(searchTerm)
            );
        });
    }else{
        return logctmo.value
    }
});
//-----------------------------------------------------------------
const filteredCarga2 = computed(() => {
    if (search.value === '') {
        return logdemo.value;

    } else if (options.value == 'Logdemo') {
        const searchTerm = search.value.toLowerCase();

        return logdemo.value.filter(elm1 => {
            return (
                elm1.secuencia?.toLowerCase().includes(searchTerm) ||
                elm1.orden_produccion?.toLowerCase().includes(searchTerm) ||
                elm1.pallets?.toLowerCase().includes(searchTerm) ||
                elm1.cajas?.toLocaleLowerCase().includes(searchTerm) ||
                elm1.peso?.toLowerCase().includes(searchTerm) ||
                elm1.pallet_desp?.toLocaleLowerCase().includes(searchTerm) ||
                elm1.peso_desp?.toLocaleLowerCase().includes(searchTerm)
            );
        });
    }else{
        return logdemo.value
    }
});

//const FunClick = (fe: any, op: any, nv: any) => {
//  let fecha = fe;
//  let operador = op;
//  let numero_vuelo = nv;
   
//----------------------------------------------------------------
// Estado del formulario y la data
//const formData = ref({
//  base_datos: '',
//  tipo_base_datos: '',
//  servidor_bdatos: '',
//  hostname: '',
//  ip_address: '',
//  servicio: '',
//  puerto: '',
//  protocolo: ''
//});

// Variables de control
const dataList = ref<any[]>([]); // Lista de datos de la API
const currentIndex = ref(0);
const isEditing = ref(false);
const isSearching = ref(false);
const isInserting = ref(false);
const isDeleting = ref(false);
const canNavigate = ref(false);
const onlyRead = ref(true);
const ButtonText = ref('Conf')
const ButtonText2 = ref('Complto')
const ButtonText3 = ref('Calcula')
const ButtonText4 = ref('Anular')

// Deshabilita los botones de btn-group2 si no está en modo búsqueda o insercion
const canUseGroup2 = computed(() => isSearching.value || isInserting.value || isEditing.value || isDeleting.value);

//boton principal que controla el submit
//carga de las ayudas
const codigos = ref<any[]>([]);
onMounted( async () => {
  const responseC = await axios.get(dUrl.urlGlobal + '/api2/logtral/filter?status=A')
  codigos.value = responseC.data
    //getCarcmani();
    //getCardmani("1", "1", "1", null);
  
});

//computados de las ayudas
const descripcionCodigo = computed(() => {
  const encontrado = codigos.value.find(op => op.codigo === formData.value.codigo)
  return encontrado ? encontrado.descripcion : '' 
})

getLogctmo()
getLogdemo("1", "1", null, "1", "1", "1", null)

id_ref.value = null

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
  overflow: scroll;

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
.card {
  width: 85%;
  height: 200px;
  min-width: min-content;
  box-sizing: border-box;
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
  height: 250px;
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

.div-buttom{
  max-width: 200px;
  overflow: hidden;
}
</style>