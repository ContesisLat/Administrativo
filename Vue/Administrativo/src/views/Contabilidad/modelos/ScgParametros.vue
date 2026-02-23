<template>
  <div class="glass-wrapper">

    <!-- HEADER -->
    <div class="top-bar">
      <div class="title">Naturaleza</div>

      <div class="search-box">
        <svg viewBox="0 0 16 16" width="14">
          <path
            d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"
            fill="currentColor" />
        </svg>
        <input type="search" placeholder="Buscar..." v-model="search" />
      </div>
    </div>

    <!-- TABLE -->
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Naturaleza</th>
            <th>Nombre</th>
            <th>Cargo</th>
            <th>Descripción</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="elm in filteredCarga" :key="elm.naturaleza"
            @click="FunClick(elm.naturaleza, elm.nombre, elm.status)">
            <td>{{ elm.naturaleza }}</td>
            <td>{{ elm.nombre }}</td>
            <td>{{ elm.cargo }}</td>
            <td>{{ elm.nom_cargo }}</td>
            <td>
              <span class="status-pill">
                {{ elm.nom_status }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- ACTION BUTTONS -->
    <div class="actions">
      <button class="action-btn insert" @click.prevent="CbtnIn">Insertar</button>
      <button class="action-btn update" @click.prevent="CbtnUp">Actualizar</button>
      <button class="action-btn delete" @click.prevent="CbtnDl">Eliminar</button>
    </div>

    <!-- MODALES -->
    <UpCarNatur v-if="btnUp" :natur="natur" :nombre="nombre" :status="status" :btnUp="btnUp"
      @updateProps="updatePropsValue" />

    <InCarNatur v-if="btnIn" :btnIn="btnIn" @insertProps="insertPropsValue" />

    <DlCarNatur v-if="btnDl" :btnDl="btnDl" :natur="natur" @deleteProps="deletePropsValue" />

  </div>
</template>


<script lang="ts" setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { Natur } from '@/interface/interfaces'
//import UpCarNatur from 'UpCarNatur.vue';

import { UrlGlobal } from '@/store/dominioGlobal';

const dUrl = UrlGlobal()

//carga de data-------------------------------------------------------
const carga = ref<Array<Natur>>([]);
const search = ref('')

const getCarga = () => {
  axios.get(dUrl.urlGlobal + '/api2/carnatur/')
    .then(response => {
      carga.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching cargos:', error);
    });
};

const filteredCarga = computed(() => {
  if (search.value === '') {
    // Si no hay nada en la búsqueda, retornar todos los registros
    return carga.value;
  } else {
    // Convertir el término de búsqueda a minúsculas para hacer la búsqueda insensible a mayúsculas
    const searchTerm = search.value.toLowerCase();

    // Filtrar los registros que coincidan con el valor de búsqueda en cualquiera de los campos
    return carga.value.filter(elm => {
      return (
        elm.naturaleza?.toLowerCase().includes(searchTerm) ||
        elm.nombre?.toLowerCase().includes(searchTerm) ||
        elm.cargo?.toLowerCase().includes(searchTerm) ||
        elm.nom_cargo?.toLowerCase().includes(searchTerm) ||
        elm.nom_status?.toLowerCase().includes(searchTerm)
      );
    });
  }
});
//----------------------------------------------------------------------

//funcion de los botones y las extenciones de Insert,delete,update----------------
let natur: any
let nombre: any
let status: any
let btnUp = ref(false);//variable para mostrar modal de update
let clickUp = ref(false)//variable para activar el click de Up
let btnIn = ref(false);//variable modal insert
let btnDl = ref(false);//variable para mostrar modal del delete
let clickDl = ref(false);//variable para activar el click del delete

//funciones q activan el click y en el caso del insert muestran el modal
const CbtnUp = () => {
  clickUp.value = !clickUp.value
  clickDl.value = false
}
const CbtnIn = () => {
  btnIn.value = !btnIn.value
  clickUp.value = false
  clickDl.value = false
}

const CbtnDl = () => {
  clickDl.value = !clickDl.value
  clickUp.value = false
}
//funcion principal para el funcionamiento de el update y delete cuando uno de los 2 este activado
const FunClick = (n: any, nm: any, st: any) => {
  natur = n;
  nombre = nm;
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

//funciones de emits para actualizar las variables y cierre los modales activos sea de update o insert
function updatePropsValue(newValue: boolean) {
  btnUp.value = newValue
  getCarga()
}
function insertPropsValue(newValue: boolean) {
  btnIn.value = newValue
  getCarga();
}

function deletePropsValue(newValue: boolean) {
  btnDl.value = newValue
  getCarga()
}
//-------------------------------------------------------------------------------

onMounted(() => {
  //getCarga();
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

</style>