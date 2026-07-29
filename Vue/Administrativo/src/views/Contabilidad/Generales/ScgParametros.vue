<template>
  <div class="glass-wrapper">

    <!-- HEADER -->
    <div class="top-bar">
      <div class="title">Parametros</div>

      <div class="search-box">
        <svg viewBox="0 0 16 16" width="14">
          <path
            d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"
            fill="currentColor" />
        </svg>
        <input type="search" placeholder="Buscar..." v-model="search" />
      </div>
    </div>

    <!-- ================= DETALLE ================= -->
    <div class="detalle-table">
        <div class="table-header-actions">
            <button v-if="mode === 'insert'" class="action-btn insert" @click="addRow" aria-label="Agregar Fila">
                + Agregar Fila
            </button>
        </div>
        <table>
            <thead>
                <tr>
                  <th class="resizable">Parámetro <span class="resizer" @mousedown="startResize($event)"
                          aria-label="Redimensionar columna"></span></th>
                  <th class="resizable">Descripción<span class="resizer" @mousedown="startResize($event)"
                          aria-label="Redimensionar columna"></span></th>
                  <th class="resizable">Valor<span class="resizer" @mousedown="startResize($event)"
                          aria-label="Redimensionar columna"></span></th>
                  <th class="resizable">Estado <span class="resizer" @mousedown="startResize($event)"
                          aria-label="Redimensionar columna"></span></th>
                  <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(fila, index) in registros" :key="index">
                    <td>
                      <select id="segpara" v-model="fila.parametro" :disabled="mode === 'view'" required>
                        <option v-for="i in segpara" :key="i.parametro" :value="i.parametro">
                            {{ i.parametro }}
                        </option>
                      </select>
                    </td>
                    <td>
                      <input v-model="fila.nom_parametro" readonly />  
                    </td>
                    <td>
                        <input v-model="fila.valor" :disabled="mode === 'view'" required />
                    </td>
                    <td>
                        <select v-model="fila.status" :disabled="mode === 'view'" required>
                            <option value="A">Activo</option>
                            <option value="I">Inactivo</option>
                        </select>
                    </td>
                    <td v-if="mode === 'view'">
                      <button class="action-btn delete" @click="removeRow(index)" aria-label="Eliminar Fila">
                                X
                      </button>
                    </td>
                    <td v-if="mode === 'insert'">
                      <button class="action-btn insert" @click="handleInsert()" aria-label="Insertar Fila">
                                Adición
                      </button>
                    </td>
                    <td v-if="mode === 'edit'">
                        <button class="action-btn edit" @click="handleUpdate" aria-label="Actualizar Fila">
                            Actualiza
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    
    <!-- ================= FOOTER ACCIONES ================= -->
   <!-- ACTION BUTTONS -->
    <div class="actions">
      <button class="action-btn insert" @click.prevent="Insertar">Insertar</button>
      <button class="action-btn update" @click.prevent="Actualiza">Actualizar</button>
      <button class="action-btn update" @click.prevent="Reinicio">Cancelar</button>
      <button class="action-btn delete" @click.prevent="CbtnDl">Eliminar</button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { Segpaag } from '@/interface/interfaces'
import { Segpara } from '@/interface/interfaces'
//import UpCarNatur from 'UpCarNatur.vue';

import { UrlGlobal } from '@/store/dominioGlobal';


import { useDateTimeStore } from '@/store/dateTimeStore';
import { userGlobalStore } from '@/store/userGlobal';
import { useAlert } from '@/store/useAlert';
import { durationValueToCss } from 'ag-grid-community/dist/types/src/agStack/theming/themeTypeUtils';

// URL y Stores
const dUrl = UrlGlobal()
const userStore = userGlobalStore();
const dateTimeStore = useDateTimeStore();

// Alerta de feedback
const { success, error, question, warning } = useAlert();

// Modo operacion
type Mode = 'view' | 'insert' | 'edit' | 'delete' | 'search';
const mode = ref<Mode>('view');
const isProcessing = ref(false);

// Computadas para manejar la UI
const isViewMode = computed(() => mode.value === 'view');
const actionLabel = computed(() => {
    switch (mode.value) {
        case 'insert': return 'Insertar';
        case 'edit': return 'Actualizar';
        case 'delete': return 'Eliminar';
        case 'search': return 'Buscar';
        default: return '';
    }
});
//carga de data-------------------------------------------------------
const segpaag = ref<Array<Segpaag>>([]);
const segpara = ref<Array<Segpara>>([])
const search = ref('')
const registros = ref<Registro[]>([]);

const canNavigate = ref(false);

interface Registro {
    parametro: string;
    nom_parametro: string;
    valor: string;
    status: string;
    nom_status: string;
}
// envio del insert a la tabla en la base de datos a traves de la api en django
const handleClick = async () => {
    dateTimeStore.refreshDateTime();
    console.log(dateTimeStore.formattedDate)
}

const handleSubmit = async () =>{
    dateTimeStore.refreshDateTime();
    console.log(dateTimeStore.formattedDate)
    const data = {
        model:"segpaag",
        data:{
            compania: userStore.Compania,
            agencia: userStore.Agencia,
            aplicacion: 'SCG',
            creado_por:userStore.globalUser,
            fecha_creado:dateTimeStore.formattedDate,
            hora_creado:dateTimeStore.formattedTime
        }
    }
    try {
        const response = await fetch(dUrl.urlGlobal +'/api3/insert/',{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        if(response.ok){
            const responseData = await response.json()
            console.log("Insercion exitosa:",responseData)
            handleClick()
        }else{
            console.error("Error al insertar en la base de datos:",response.statusText)
        }
    }catch (error){
        console.error("error de red:",error)
    }
}
//---------------------------------------------------------------------------------------------
const getSegpaag = () => {
  axios.get(dUrl.urlGlobal + '/api3/segpaag/')
    .then(response => {
      registros.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching cargos:', error);
    });
};

const filteredCarga = computed(() => {
  if (search.value === '') {
    // Si no hay nada en la búsqueda, retornar todos los registros
    return registros.value;
  } else {
    // Convertir el término de búsqueda a minúsculas para hacer la búsqueda insensible a mayúsculas
    const searchTerm = search.value.toLowerCase();

    // Filtrar los registros que coincidan con el valor de búsqueda en cualquiera de los campos
    return registros.value.filter(elm => {
      return (
        elm.parametro?.toLowerCase().includes(searchTerm) ||
        elm.nom_parametro?.toLowerCase().includes(searchTerm) ||
        elm.valor?.toLowerCase().includes(searchTerm) ||
        elm.nom_status?.toLowerCase().includes(searchTerm)
      );
    });
  }
});

// Función para validar que no haya cargos repetidos
function valida(arr: string[]): boolean { return new Set(arr).size === arr.length }

// Función para manejar la inserción
async function handleInsert() {
    if (isProcessing.value) return;
    isProcessing.value = true;

    const detallesActivos = registros.value.filter(r => r.status !== 'I');
    if (detallesActivos.length === 0) {
        error('Por favor, ingrese al menos un parametro');
        return;
    }

    if (!valida(detallesActivos.map(r => r.parametro))) {
        error('Existen parametros repetidos...');
        return;
    }

    // Confirmación de inserción
    const result = await question('Se va a insertar el registro.', '¿Deseas insertar este registro?');
    if (!result.isConfirmed) return;

    try {
        // Insertamos los detalles
        for (const fila of detallesActivos) {
            const dataDetalle = { model: "segpaag", data: { ...fila, creado_por: userStore.globalUser, fecha_creado: dateTimeStore.formattedDate, hora_creado: dateTimeStore.formattedTime } }
            await fetch(`${dUrl.urlGlobal}/api3/insert, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(dataDetalle) }`)
        }

        success('Datos insertados correctamente', 'Inserción exitosa');
        mode.value = 'view';
        resetAll(); // Limpiamos los campos
    } catch (err: any) {
        error('Error inesperado al insertar')

    } finally {
        isProcessing.value = false
    }
}

// Función para manejar la actualización de los detalles
const upsertDetalle = async (fila: { parametro: string; valor: any; status: any }) => {
    if (!fila.parametro) return;
    try {
        const response = await axios.post( `${dUrl.urlGlobal}/api3/query`, { tabla: 'segpaag', filtro: { parametro: fila.parametro } });
        const existe = response.data.length > 0;
        if (!existe) {
            const dataInsert = { tabla: 'segpaag', data: { ...fila, creado_por: userStore.globalUser, fecha_creado: dateTimeStore.formattedDate, hora_creado: dateTimeStore.formattedTime } };
            const resInsert = await fetch( `${dUrl.urlGlobal}/api3/insert/, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(dataInsert) }`);
            if (!resInsert.ok) error(`Error insertando el parámetro ${fila.parametro}`);
        } else {
            const dataUpdate = {
                table: 'segpaag',
                filters: {
                    parametro: fila.parametro
                },
                data: {
                    ...fila,
                    modificado_por: userStore.globalUser,
                    fecha_status: dateTimeStore.formattedDate,
                    hora_status: dateTimeStore.formattedTime
                }
            };

            Object.keys(dataUpdate.data).forEach(k => {
                if (dataUpdate.data[k as keyof typeof dataUpdate.data] === undefined) delete dataUpdate.data[k as keyof typeof dataUpdate.data];
            });

            const resUpdate = await axios.post( `${dUrl.urlGlobal}/update/, dataUpdate`);
            if (resUpdate.status !== 200) error(`Error actualizando el parametro ${fila.parametro}`);
        }
    } catch (err: any) {
        error(err.response?.data?.detail || `Error procesando el parametro ${fila.parametro}`);
    }
};
// Función para manejar la actualización 
const handleUpdate = async () => {
    if (isProcessing.value) return;
    isProcessing.value = true;

    try {
        // Actualizamos los detalles de los registros
        for (const fila of registros.value) await upsertDetalle(fila);

        success('Datos actualizados correctamente', 'Actualización exitosa');
        mode.value = 'search';
    } catch (err: any) {
        error(err.response?.data?.detail || 'Error al actualizar');
    } finally {
        isProcessing.value = false
    }
};
// Función para manejar la eliminación de un registro
const handleDelete = async () => {
    if (isProcessing.value) return;
    isProcessing.value = true;

    const result = await question('Se va a inactivar el registro.', '¿Deseas inhabilitar este registro?');
    if (!result.isConfirmed) return;

    try {
        for (const fila of registros.value) {
            if (!fila.parametro) continue;
            try {
                await axios.post(`${dUrl.urlGlobal}/api2/update/, {
                    table: 'segpaag',
                    filters: { parametro: fila.parametro },
                    data: { status: 'I' }
                }`);
            } catch (err: any) {
                console.log(err);
            }
        }

        success('Parámetro inactivado correctamente', 'Acción exitosa');
        mode.value = 'search';
    } catch (err: any) {
        error(err.response?.data?.detail || 'Error inesperado');
    } finally {
        isProcessing.value = false
    }
};
//----------------------------------------------------------------------
// Función para manejar cualquier acción según el modo
async function handleAction() {
    switch (mode.value) {
        case 'insert':
            await handleInsert();
            break;
        case 'edit':
            await handleUpdate();
            break;
        case 'delete':
            await handleDelete();
            break;
        //case 'search':
        //    await handleSearch();
        //    break;
        default:
            break;
    }
}

// ================= RESET ALL =================
const resetAll = () => {

    if (mode.value === 'edit' || mode.value === 'delete') {
        // Regresar a search manteniendo datos
        mode.value = 'search';
        return;
    }

    // Para insert y search sí limpiamos todo
    mode.value = 'view';
    registros.value = [];
  
    canNavigate.value = false;
};

//funcion de los botones y las extenciones de Insert,delete,update----------------
let parametro: any
let nom_parametro: any
let valor: any
let status: any
let btnUp = ref(false);//variable para mostrar modal de update
let clickUp = ref(false)//variable para activar el click de Up
let btnIn = ref(false);//variable modal insert
let btnDl = ref(false);//variable para mostrar modal del delete
let clickDl = ref(false);//variable para activar el click del delete

//funciones q activan el click y en el caso del insert muestran el modal
const Reinicio = () => {
   mode.value = 'view'
}
const Actualiza = () => {
   mode.value = 'edit'
}
const Insertar = () => {
  mode.value = 'insert'
}

const CbtnDl = () => {
  clickDl.value = !clickDl.value
  clickUp.value = false
}
//funcion principal para el funcionamiento de el update y delete cuando uno de los 2 este activado
const FunClick = (n: any, nm: any, st: any) => {
  parametro = n;
  nom_parametro = nm;
  status = st;

  if (clickUp.value == true) {
    btnUp.value = !btnUp.value
    clickUp.value = !clickUp.value
  }
  if (clickDl.value == true) {
    btnDl.value = !btnDl.value
    clickDl.value = !clickDl.value
  }
}

function MuestraNom(indx: number) {
  const elemento = registros.value[indx]

   

}


//funciones de emits para actualizar las variables y cierre los modales activos sea de update o insert
function updatePropsValue(newValue: boolean) {
  btnUp.value = newValue
  getSegpaag()
}
function insertPropsValue(newValue: boolean) {
  btnIn.value = newValue
  getSegpaag();
}

function deletePropsValue(newValue: boolean) {
  btnDl.value = newValue
  getSegpaag()
}
//-------------------------------------------------------------------------------

/* ================= RESIZE COLUMNAS ================= */

let currentTh: HTMLElement | null = null
let startX = 0// ================= AGREGAR / ELIMINAR FILAS =================
function addRow() {
    registros.value.push({
        parametro: '',
        nom_parametro: '',
        valor: '',
        status: 'A',
        nom_status: 'Activo'
    });


}

function removeRow (index: number) {
  //const result =  question('Se va a eliminar la línea.', '¿Desea continuar?');
  
  //if (!result.catch) return;
    registros.value.splice(index, 1);
    mode.value = 'view'
    //recalcularTotal(); // Recalcular el total del servicio
}

let startWidth = 0

function startResize(event: MouseEvent) {
    currentTh = (event.target as HTMLElement).parentElement as HTMLElement
    startX = event.pageX
    startWidth = currentTh.offsetWidth

    document.addEventListener('mousemove', resizeColumn)
    document.addEventListener('mouseup', stopResize)
}

function resizeColumn(event: MouseEvent) {
    if (!currentTh) return
    const newWidth = startWidth + (event.pageX - startX)
    currentTh.style.width = newWidth + 'px'
}

function stopResize() {
    document.removeEventListener('mousemove', resizeColumn)
    document.removeEventListener('mouseup', stopResize)
    currentTh = null
}

onMounted(async() => {
  try {
        segpara.value = (await axios .get(`${dUrl.urlGlobal}/api/segpara`)).data;
    } catch (err: any) {
        error('Error al cargar datos iniciales');
    }
  getSegpaag();
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

.glass-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  font-family: 'Poppins', sans-serif;
  color: #2c2c2c;
}

/* =========================
   TOP BAR
========================= */

.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 22px;
}

.title {
  font-size: 18px;
  font-weight: 600;
  letter-spacing: 0.4px;
  color: #3a3a3a;
}

/* =========================
   SEARCH BOX PREMIUM
========================= */

.search-box {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 9px 16px;
  border-radius: 16px;

  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);

  border: 1px solid rgba(255, 255, 255, 0.9);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.06);

  transition: all 0.25s ease;
}

.search-box:focus-within {
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
  transform: translateY(-1px);
}

.search-box svg {
  color: #777;
}

.search-box input {
  border: none;
  outline: none;
  background: transparent;
  font-size: 14px;
  width: 180px;
  color: #333;
  transition: 0.2s ease;
}

/* =========================
   TABLE CONTAINER
========================= */

.table-wrapper {
  flex: 1;
  overflow: auto;

  border-radius: 20px;

  background: rgba(255, 255, 255, 0.55);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);

  border: 1px solid rgba(255, 255, 255, 0.75);

  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.06);

  transition: 0.3s ease;
}

/* =========================
   TABLE
========================= */

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

thead {
  background: rgba(255, 255, 255, 0.75);
  position: sticky;
  top: 0;
  backdrop-filter: blur(10px);
}

th {
  text-align: left;
  padding: 16px 14px;
  font-weight: 600;
  font-size: 13px;
  color: #666;
  letter-spacing: 0.4px;
}

td {
  padding: 16px 14px;
  border-top: 1px solid rgba(0, 0, 0, 0.04);
  color: #444;
}

tbody tr {
  cursor: pointer;
  transition: all 0.25s ease;
}

tbody tr:hover {
  background: rgba(255, 255, 255, 0.8);
  transform: scale(1.002);
}

/* =========================
   STATUS PILL
========================= */

.status-pill {
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;

  background: rgba(0, 123, 255, 0.12);
  color: #007bff;
}

/* =========================
   ACTION BUTTONS
========================= */

.actions {
  display: flex;
  justify-content: flex-end;
  gap: 14px;
  margin-top: 22px;
}

.action-btn {
  padding: 10px 22px;
  border-radius: 18px;
  border: none;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;

  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);

  transition: all 0.25s ease;
}

/* Insert */
.insert {
  background: rgba(93, 116, 183, 0.15);
  color: #3f5fa8;
}

/* Update */
.update {
  background: rgba(188, 211, 74, 0.25);
  color: #7a941a;
}

/* Delete */
.delete {
  background: rgba(217, 75, 106, 0.18);
  color: #c23c5d;
}

/* Hover effect premium */
.action-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
}


.resizable {
    position: relative;
}

.resizer {
    position: absolute;
    right: 0;
    top: 0;
    width: 6px;
    height: 100%;
    cursor: col-resize;
    user-select: none;
}

</style>