<template>

  <body>
    <div class="Card">
      <section class="layout">
        <div class="header">
          <div class="btn-search">
            <span><svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" fill="currentColor"
                class="bi bi-search" viewBox="0 0 16 16">
                <path
                  d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0" />
              </svg></span>
            <input type="search" id="search" placeholder="Buscar"
              style="background-color: transparent; border: none; outline: none; color: white;" autocomplete="off" v-model="search">
          </div>
        </div>
        <div class="container">
          <div class="row">
            <div class="col d-flex flex-column justify-content-center align-items-center">
              <h3><strong>Naturaleza</strong></h3>
              <div class="card overflow-scroll">
                <table class="table table-hover table-sm">
                  <thead>
                    <tr>
                      <th>Naturaleza</th>
                      <th>Nombre</th>
                      <th>Cargo</th>
                      <th>Descripcion</th>
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
                      <td>{{ elm.nom_status }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="btn-group">
                <button class="btn-insert" @click.prevent="CbtnIn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-upload" viewBox="0 0 16 16">
                    <path
                      d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5" />
                    <path
                      d="M7.646 1.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 2.707V11.5a.5.5 0 0 1-1 0V2.707L5.354 4.854a.5.5 0 1 1-.708-.708z" />
                  </svg>
                </button>
                <button class="btn-update" @click.prevent="CbtnUp">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-pencil-square" viewBox="0 0 16 16">
                    <path
                      d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
                    <path fill-rule="evenodd"
                      d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z" />
                  </svg>
                </button>
                <button class="btn-delete" @click.prevent="CbtnDl">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-trash3" viewBox="0 0 16 16">
                    <path
                      d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5M11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47M8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
        <UpCarNatur v-if="btnUp" :natur="natur" :nombre="nombre" :status="status" :btnUp="btnUp"
          @updateProps="updatePropsValue" />
        <InCarNatur v-if="btnIn" :btnIn="btnIn" @insertProps="insertPropsValue" />
        <DlCarNatur v-if="btnDl" :btnDl="btnDl" :natur="natur" @deleteProps="deletePropsValue" />
      </section>
    </div>
  </body>
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
  gap: 8px;
}

.header {
  display: flex;
  justify-content: right;
  align-items: right;
  grid-area: header;
}

.container {
  grid-area: container;
}

.card {
  width: 85%;
  height: 250px;
  min-width: min-content;
  box-sizing: border-box;
}

.btn-search {
  border: none;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(10px);
  color: white;
  padding-left: 3px;
  justify-content: space-between;
  display: flex;
  gap: 4px;
  min-width: min-content;
}

.btn-search:focus {
  outline: none;
}

.btn-group {
  display: flex;
  justify-content: flex-end;
  gap: 20px;
  margin-top: 20px;
}

.btn-group button {
  border: none;
  border-radius: 20px;
}

.btn-delete:hover,
.btn-delete:focus {
  background: #d94b6a;
  color: white;
}

.btn-update:hover,
.btn-update:focus {
  background: #bcd34a;
  color: white;
}

.btn-insert:hover,
.btn-insert:focus {
  background: #5d74b7;
  color: white;
}
</style>