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

    <div v-if="mode !== 'none'" class="mode-controls">

      <!-- INSERT CONTROLS -->
      <template v-if="mode === 'insert'">

        <button class="action-btn insert" @click="addRow">
          Agregar fila
        </button>

        <button class="action-btn update" @click="confirmInsert">
          Insertar contenido
        </button>

      </template>

      <!-- GLOBAL CANCEL -->
      <button class="action-btn delete" @click="cancelMode">
        Cancelar
      </button>

    </div>

    <!-- TABLE -->
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th @click="sortBy('naturaleza')">Naturaleza <span>{{ getSortIcon('naturaleza') }}</span></th>
            <th @click="sortBy('nombre')">Nombre <span>{{ getSortIcon('nombre') }}</span></th>
            <th @click="sortBy('cargo')">Cargo <span>{{ getSortIcon('cargo') }}</span></th>
            <th @click="sortBy('nom_cargo')">Descripción <span>{{ getSortIcon('nom_cargo') }}</span></th>
            <th @click="sortBy('nom_status')">Status <span>{{ getSortIcon('nom_status') }}</span></th>
            <th v-if="mode !== 'none'">Acción</th>
          </tr>
        </thead>

        <tbody>

          <!-- EXISTING ROWS -->
          <tr v-for="(elm, index) in filteredCarga" :key="index">

            <td>{{ elm.naturaleza }}</td>

            <td>
              <input v-if="isEditing(elm)" v-model="elm.nombre" />
              <span v-else>{{ elm.nombre }}</span>
            </td>

            <td>
              <input v-if="isEditing(elm)" v-model="elm.cargo" />
              <span v-else>{{ elm.cargo }}</span>
            </td>

            <td>
              <input v-if="isEditing(elm)" v-model="elm.nom_cargo" />
              <span v-else>{{ elm.nom_cargo }}</span>
            </td>

            <td>

              <!-- EDIT MODE -->
              <select v-if="isEditing(elm)" v-model="elm.nom_status" class="status-select">
                <option v-for="opt in statusOptions" :key="opt.value" :value="opt.label">
                  {{ opt.label }}
                </option>
              </select>

              <!-- NORMAL MODE -->
              <span v-else class="status-pill">
                {{ elm.nom_status }}
              </span>

            </td>

            <!-- ACTIONS UPDATE -->
            <td v-if="mode === 'update'">

              <button v-if="editingRow !== elm.naturaleza" class="row-btn edit" @click="enableEdit(elm)">
                Editar
              </button>

              <div v-else>
                <button class="row-btn save" @click="confirmUpdate(elm)">Guardar</button>
                <button class="row-btn cancel" @click="cancelEdit">Cancelar</button>
              </div>

            </td>

            <!-- ACTIONS DELETE -->
            <td v-if="mode === 'delete'">
              <button class="row-btn delete" @click="confirmDelete(elm)">
                Eliminar
              </button>
            </td>

          </tr>

          <!-- NEW ROWS -->
          <tr v-for="(row, i) in newRows" :key="'new' + i" class="new-row">

            <td>
              <input v-model="row.naturaleza" />
            </td>

            <td>
              <input v-model="row.nombre" />
            </td>

            <td>
              <input v-model="row.cargo" />
            </td>

            <td>
              <input v-model="row.nom_cargo" />
            </td>

            <td>
              <select v-model="row.nom_status" class="status-select">
                <option disabled value="">Seleccione</option>
                <option v-for="opt in statusOptions" :key="opt.value" :value="opt.label">
                  {{ opt.label }}
                </option>
              </select>
            </td>

            <td>
              <button class="row-btn delete" @click="removeNewRow(i)">Eliminar</button>
            </td>

          </tr>

        </tbody>
      </table>
    </div>
    <!-- MODE BUTTONS -->
    <div class="actions">
      <button class="action-btn insert" @click="exportToExcel">Exportar Excel</button>
      <button class="action-btn insert" :class="{ active: mode === 'insert' }" @click="activateInsert">Insertar</button>
      <button class="action-btn update" :class="{ active: mode === 'update' }"
        @click="activateUpdate">Actualizar</button>
      <button class="action-btn delete" :class="{ active: mode === 'delete' }" @click="activateDelete">Eliminar</button>
    </div>

  </div>
</template>


<script lang="ts" setup>

import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import { Natur } from '@/interface/interfaces'
import { UrlGlobal } from '@/store/dominioGlobal'
import { useAlert } from '@/store/useAlert'
import { useDateTimeStore } from '@/store/dateTimeStore';
import { userGlobalStore } from '@/store/userGlobal';

const { success, error, question, warning } = useAlert()

const dUrl = UrlGlobal()
const dateTimeStore = useDateTimeStore();
const userStore = userGlobalStore();

/* =========================
   DATA
========================= */

const carga = ref<Array<Natur>>([])
const search = ref('')

const mode = ref<'none' | 'insert' | 'update' | 'delete'>('none')

const editingRow = ref<string | undefined>(undefined)

const newRows = ref<Array<any>>([])


/* =========================
   ORDER BY
========================= */
const sortKey = ref('')                // columna actual que se está ordenando
const sortOrder = ref<'asc' | 'desc'>('asc') // orden actual: ascendente o descendente

// Función que cambia el orden al hacer click en un th
const sortBy = (key: string) => {
  if (sortKey.value === key) {
    // Si ya está ordenando por esta columna, invertir orden
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
  } else {
    // Si es nueva columna, ordenar asc
    sortKey.value = key
    sortOrder.value = 'asc'
  }
}

// Icono visual de la columna ordenada
const getSortIcon = (key: string) => {
  if (sortKey.value !== key) return ''
  return sortOrder.value === 'asc' ? '▲' : '▼'
}


/* =========================
 STATUS OPTIONS
========================= */

const statusOptions = ref([
  { value: 'A', label: 'Activo' },
  { value: 'I', label: 'Inactivo' }
])

/* =========================
   GET DATA
========================= */

const getCarga = () => {

  axios.get('https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api2/carnatur/')
    .then(res => {
      carga.value = res.data
    })
    .catch(err => {
      console.error(err)
    })

}

/* =========================
   SEARCH FILTER
========================= */

const filteredCarga = computed(() => {

  let data = carga.value  // 1 Empezamos con todos los datos

  // 2 FILTRO POR BÚSQUEDA
  if (search.value) {
    const term = search.value.toLowerCase()
    data = data.filter(elm =>
      elm.naturaleza?.toLowerCase().includes(term) ||
      elm.nombre?.toLowerCase().includes(term) ||
      elm.cargo?.toLowerCase().includes(term) ||
      elm.nom_cargo?.toLowerCase().includes(term) ||
      elm.nom_status?.toLowerCase().includes(term)
    )
  }

  // 3 ORDENAMIENTO
  if (sortKey.value) {
    data = [...data].sort((a: any, b: any) => {
      const valA = a[sortKey.value] || '' // valor columna a
      const valB = b[sortKey.value] || '' // valor columna b

      if (sortOrder.value === 'asc') return valA > valB ? 1 : -1
      else return valA < valB ? 1 : -1
    })
  }

  return data
})

/* =========================
   MODE CONTROL
========================= */

const activateInsert = () => {
  mode.value = 'insert'
  newRows.value = []
  editingRow.value = undefined
}

const activateUpdate = () => {
  mode.value = 'update'
  newRows.value = []
}

const activateDelete = () => {
  mode.value = 'delete'
  newRows.value = []
}

const cancelMode = () => {
  mode.value = 'none'
  newRows.value = []
  editingRow.value = undefined
}

/* =========================
   INSERT NEW ROW
========================= */

const addRow = () => {

  newRows.value.push({
    naturaleza: '',
    nombre: '',
    cargo: '',
    nom_cargo: '',
    nom_status: ''
  })

}

/* =========================
   DELETE NEW ROW
========================= */

const removeNewRow = (index: number) => {

  newRows.value.splice(index, 1)

}

/* =========================
   INSERT
========================= */

const confirmInsert = async () => {

  const result = await question('¿Insertar registros nuevos?')

  if (!result.isConfirmed) return

  insertRows()

}

const insertRows = async () => {
  try {
    for (const row of newRows.value) {
      // Validar campos obligatorios
      if (!row.naturaleza || !row.nombre) {
        warning("Naturaleza y Nombre son obligatorios")
        return
      }

      // Preparar el objeto completo a enviar
      const data = {
        model: "carnatur",
        data: {
          naturaleza: row.naturaleza,
          nombre: row.nombre,
          cargo: row.cargo || "",
          nom_cargo: row.nom_cargo || "",
          nom_status: row.nom_status || "",
          status: row.nom_status || "",
          creado_por: userStore.globalUser,
          fecha_creado: dateTimeStore.formattedDate,
          hora_creado: dateTimeStore.formattedTime
        }
      }

      // Enviar fila al backend
      await axios.post(dUrl.urlGlobal + "/api2/insert/", data)
    }

    success("Registros insertados correctamente")

    // Limpiar las filas nuevas
    newRows.value = []

    // Recargar tabla
    await getCarga()

    // Salir del modo insert
    cancelMode()
  } catch (err) {
    console.error(err)
    error("No se pudieron insertar los registros")
  }
}

/* =========================
   UPDATE
========================= */

const enableEdit = (row: Natur) => {
  editingRow.value = row.naturaleza
}

const cancelEdit = () => {
  editingRow.value = undefined
}

const isEditing = (row: Natur) => {
  return editingRow.value === row.naturaleza
}

const confirmUpdate = async (row: Natur) => {

  const result = await question(
    `¿Actualizar el registro ${row.naturaleza}?`
  )

  if (!result.isConfirmed) return

  updateRow(row)

}

const updateRow = async (row: Natur) => {

  try {

    const dataUpdate: any = {}

    if (row.nombre) dataUpdate.nombre = row.nombre
    if (row.cargo) dataUpdate.cargo = row.cargo
    if (row.nom_cargo) dataUpdate.nom_cargo = row.nom_cargo
    if (row.nom_status) dataUpdate.status = row.nom_status

    const response = await axios.post(
      dUrl.urlGlobal + "/api2/update/",
      {
        table: "carnatur",
        filters: {
          naturaleza: row.naturaleza
        },
        data: dataUpdate
      }
    )

    success("Registro actualizado correctamente")

    editingRow.value = undefined

    await getCarga()

  } catch (err) {

    console.error(err)

    error("No se pudo actualizar el registro")

  }

}

/* =========================
   DELETE
========================= */

const confirmDelete = async (row: Natur) => {

  const result = await question(
    `¿Eliminar el registro ${row.naturaleza}?`
  )

  if (!result.isConfirmed) return

  deleteRow(row)

}

const deleteRow = async (row: Natur) => {

  try {

    const response = await axios.post(
      dUrl.urlGlobal + "/api2/delete/",
      {
        table: "carnatur",
        filters: {
          naturaleza: row.naturaleza
        }
      }
    )

    success("Registro eliminado correctamente")

    await getCarga()

    cancelMode()

  } catch (err) {

    console.error(err)

    error("No se pudo eliminar el registro")

  }

}

/* =========================
   EXPORT TO EXCEL
========================= */

import * as XLSX from 'xlsx'

const exportToExcel = () => {

  // Tomar solo los datos filtrados
  const data = filteredCarga.value.map(item => ({
    Naturaleza: item.naturaleza,
    Nombre: item.nombre,
    Cargo: item.cargo,
    Descripción: item.nom_cargo,
    Status: item.nom_status
  }))

  const worksheet = XLSX.utils.json_to_sheet(data)
  const workbook = XLSX.utils.book_new()
  XLSX.utils.book_append_sheet(workbook, worksheet, "Naturaleza")
  XLSX.writeFile(workbook, "naturaleza.xlsx")
}
/* ========================= */

onMounted(() => {
  getCarga()
})

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
   SEARCH BOX
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

  cursor: pointer;

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

/* Hover effect */
.action-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
}

/* BUTTON ACTIVE */

.action-btn.active {
  transform: scale(1.05);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
}

.mode-controls {
  display: flex;
  gap: 12px;
  margin-bottom: 15px;
}

.cancel-main {
  background: rgba(120, 120, 120, 0.18);
  color: #555;
}

/* INPUT TABLA */

td input {
  width: 100%;
  padding: 6px;
  border-radius: 8px;
  border: 1px solid #ddd;
  font-size: 13px;
}

/* NEW ROW */

.new-row {
  background: rgba(0, 123, 255, 0.05);
}

/* BUTTONS ROW */

.row-btn {
  border: none;
  padding: 6px 10px;
  border-radius: 10px;
  font-size: 12px;
  cursor: pointer;
}

.row-btn.edit {
  background: #e8f0ff;
  color: #3559c7;
}

.row-btn.save {
  background: #dff5e1;
  color: #1c7c34;
}

.row-btn.cancel {
  background: #ffe8e8;
  color: #c0392b;
}

.row-btn.delete {
  background: #ffd6d6;
  color: #c0392b;
}

/* SELECT STATUS */

.status-select {
  width: 100%;
  padding: 6px;
  border-radius: 10px;
  border: 1px solid rgba(0, 0, 0, 0.15);
  background: rgba(255, 255, 255, 0.9);
  font-size: 13px;
  outline: none;
  transition: 0.2s;
}

.status-select:focus {
  border-color: #4a6cf7;
  box-shadow: 0 0 0 2px rgba(74, 108, 247, 0.15);
}
</style>