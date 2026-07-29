<template>
    <div class="glass-wrapper">
        <!-- ================= HEADER ================= -->
        <div class="top-bar">
            <div class="title">Catálogo de Cuentas</div>
            <div class="action-group">
                <button class="action-btn insert" @click="setMode('insert')" | v-on:click="focusInput()" :disabled="!canInsert"
                    :class="{ active: mode === 'insert' }">
                    Insertar
                </button>

                <button class="action-btn search" @click="setMode('search')" :disabled="!canSearch"
                    :class="{ active: mode === 'search' }">
                    Buscar
                </button>

                <button class="action-btn update" @click="setMode('edit')" :disabled="!canEdit"
                    :class="{ active: mode === 'edit' }">
                    Editar
                </button>

                <button class="action-btn delete" @click="setMode('delete')" :disabled="!canDelete"
                    :class="{ active: mode === 'delete' }">
                    Eliminar
                </button>
                <!--button class="action-btn cancelar" @click="setMode('delete')" :disabled="!canDelete"
                    :class="{ active: mode === 'cancel' }">
                    Eliminar
                </button-->
            </div>
            <div v-if="dataList.length > 0" class="footer-navigation">
                <button @click="prevRecord" :disabled="currentIndex === 0 || isViewMode"
                    aria-label="Registro Anterior">Anterior</button>
                <button @click="nextRecord" :disabled="currentIndex === dataList.length - 1 || isViewMode"
                    aria-label="Registro Siguiente">Siguiente</button>
            </div>
        </div>

        <!-- ================= FORM ================= -->
        <div class="form-card">
            <div class="form-grid">
                <div>
                    <label for="cuenta">Cuenta</label>
                    <input type="string" id="cuenta" v-model="formData.cuenta" :readonly="mode === 'view'" required />
                </div> 
                <div>
                    <label for="uso">Estado</label>
                    <select id="uso" v-model="formData.status" :disabled="mode === 'view'" required>
                        <option value="A">Activo</option>
                        <option value="I">Inactivo</option>
                    </select>
                </div>
            </div>
            <div class="form-grid">
                <div>
                    <label for="descripcion">Descripción</label>
                    <input id="descripcion" v-model="formData.descripcion" :readonly="mode === 'view'" required />
                </div>
            </div>
            <div class="form-grid">
                <div>
                    <label for="tipo_cuenta">Tipo Cuenta</label>
                        <select id="scggcta" v-model="formData.tipo_cuenta" :disabled="mode === 'view'" required>
                            <option v-for="item in scggcta" :key="item.tipo_cuenta" :value="item.tipo_cuenta">
                                {{ item.descripcion }}
                            </option>
                    </select>
                </div>
                <div>
                    <label for="nom_naturaleza">Naturaleza</label>
                        <select id="naturaleza" v-model="formData.naturaleza" :disabled="mode === 'view'" required>
                            <option value="D">Débito</option>
                            <option value="C">Crédito</option>
                        </select> 
                </div>
            </div>
            <div class="form-grid"> 
                <div>
                    <label for="grupo_cuenta">Grupo Cuenta</label>
                        <select id="scgsgcta" v-model="formData.grupo_cuenta" :disabled="mode === 'view'" required>
                            <option v-for="dato in scgsgcta" :key="dato.grupo_cuenta" :value="dato.grupo_cuenta">
                                {{ dato.descripcion }}
                            </option>
                    </select>
                </div>
                <div>
                    <label for="nivel_cuenta">Nivel Cuenta</label>
                    <select id="scgcodi" v-model="formData.nivel_cuenta" :disabled="mode === 'view'" required>
                        <option v-for="i in scgcodi" :key="i.nivel_cuenta" :value="i.nivel_cuenta">
                            {{ i.descripcion }}
                        </option>
                    </select>
                </div>
            </div>
            <div class="form-grid">
                <div> 
                    <label for="recibe">Recibe</label>
                    <select id="recibe" v-model="formData.recibe" :disabled="mode === 'view'" required>
                        <option value="S">Sí</option>
                        <option value="N">No</option>
                    </select>
                </div>
                <div>
                    <label for="aux_interno">Aux. Interno</label>
                    <select id="aux_interno" v-model="formData.aux_interno" :disabled="mode === 'view'" required>
                        <option value="S">Sí</option>
                        <option value="N">No</option>
                    </select>
                </div>
                <div>
                    <label for="aux_externo">Aux. Externo</label>
                    <select id="aux_externo" v-model="formData.aux_externo" :disabled="mode === 'view'" required>
                        <option value="S">Sí</option>
                        <option value="N">No</option>
                    </select>
                </div>
            </div>
        </div>  

        <!-- ================= FOOTER ACCIONES ================= -->
        <div class="footer-actions" v-if="['insert', 'search', 'edit', 'delete'].includes(mode)">
            <button class="action-btn cancel" @click="resetAll" :disabled="isViewMode"
                aria-label="Cancelar">Cancelar</button>
            <button class="action-btn confirm" @click="handleAction" :disabled="isProcessing"
                :class="{ active: isProcessing }">
                {{ actionLabel }}
            </button>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import { UrlGlobal } from '@/store/dominioGlobal';
import { userGlobalStore } from '@/store/userGlobal';
import { useDateTimeStore } from '@/store/dateTimeStore';
import { useAlert } from '@/store/useAlert';
import { Scgcata, Scggcta, Scgsgcta, Scgcodi } from '@/interface/interfaces';

// Alerta de feedback
const { success, error, question, warning } = useAlert();

// URL y Stores
const dUrl = UrlGlobal();
const userStore = userGlobalStore();
const dateTimeStore = useDateTimeStore();

// Modo de operación
type Mode = 'view' | 'insert' | 'edit' | 'delete' | 'search';
const mode = ref<Mode>('view');
const isProcessing = ref(false);

const lineaArray = 0;
// Computadas para manejar la UI
const isViewMode = computed(() => mode.value === 'view');
const isInsertOrEditMode = computed(() => ['insert', 'edit'].includes(mode.value));
const isReadonly = computed(() => mode.value === 'view');
const isBusy = computed(() => ['insert', 'edit', 'delete'].includes(mode.value));
const isActionMode = computed(() => mode.value === 'insert' || mode.value === 'search');
const actionLabel = computed(() => {
    switch (mode.value) {
        case 'insert': return 'Insertar';
        case 'edit': return 'Actualizar';
        case 'delete': return 'Eliminar';
        case 'search': return 'Buscar';
        default: return '';
    }
}); 

const canInsert = computed(() =>
    mode.value === 'view' && !isProcessing.value
);

const canSearch = computed(() =>
    mode.value === 'view' && !isProcessing.value
);

const canEdit = computed(() =>
    (
        (mode.value === 'view' && canNavigate.value) ||
        (mode.value === 'search' && dataList.value.length > 0)
    ) && !isProcessing.value
);

const canDelete = computed(() =>
    (
        (mode.value === 'view' && canNavigate.value) ||
        (mode.value === 'search' && dataList.value.length > 0)
    ) && !isProcessing.value
);

function cargaLinea(nlinea: any) {
    let lineaArray = nlinea
}
// Función para cambiar el modo
function focusInput() {
    document.getElementById("tipo_cuenta")?.focus();
}

function setMode(newMode: Mode) {
    if (isProcessing.value) return;

    switch (mode.value) {

        case 'view':
            if (newMode === 'insert' || newMode === 'search') {
                mode.value = newMode;
            }
            break;

        case 'search':
            if (
                (newMode === 'edit' || newMode === 'delete') &&
                dataList.value.length > 0
            ) {
                mode.value = newMode;
            }
            break;

        case 'insert':
        case 'edit':
        case 'delete':
            // No permitir cambio hasta confirmar o cancelar
            return;

        default:
            return;
    }
}

// ================= DATOS =================
const formData = ref({
    cuenta: '',
    descripcion: '',
    naturaleza: '',
    nom_naturaleza: '',
    nivel_cuenta: '',
    tipo_cuenta: '',
    nom_tipo: '',
    grupo_cuenta: '',
    nom_grupo: '',
    recibe: '',
    aux_interno: '',
    aux_externo: '',
    status: 'A',
    nom_status: 'Activo'
});

const scgcata = ref<Scgcata[]>([]);
const scggcta = ref<Scggcta[]>([]);
const scgsgcta = ref<Scgsgcta[]>([]);
const scgcodi = ref<Scgcodi[]>([]);
 
//const Scggcta = ref<any[]>([]);

// ================= NAVEGACIÓN =================
const dataList = ref<any[]>([]);
const currentIndex = ref(0);
const canNavigate = ref(false);

// Actualiza los datos del formulario y los detalles
function updateFormData() {
    const record = dataList.value[currentIndex.value];
    if (!record) return;

    // Llenamos el formulario con la cabecera del registro
    formData.value = { ...record };
}

// ================= NAVEGACIÓN ENTRE REGISTROS =================
function prevRecord() {
    if (currentIndex.value > 0) {
        currentIndex.value--;
        updateFormData();  // Actualizamos los datos al navegar
    }
}

function nextRecord() {
    if (currentIndex.value < dataList.value.length - 1) {
        currentIndex.value++;
        updateFormData();  // Actualizamos los datos al navegar
    }
}

// Función para manejar la inserción
async function handleInsert() {
    if (isProcessing.value) return;
    isProcessing.value = true;

    if (!formData.value.cuenta || !formData.value.descripcion ||
        !formData.value.naturaleza || !formData.value.nivel_cuenta ||
        !formData.value.tipo_cuenta || !formData.value.grupo_cuenta ||
        !formData.value.recibe || !formData.value.aux_interno ||
        !formData.value.aux_externo || !formData.value.status) {
        error('Complete todos los campos obligatorios');
        isProcessing.value = false;
        return;
    }

    try {
        const response = await axios.post(dUrl.urlGlobal + '/api3/query', { tabla: 'scgcata', filtro: { cuenta: formData.value.cuenta}});
        const existe = response.data.length > 0;
        if (existe) {
            error('Cuenta Contable ya existe...')
            return
        }
    }
    catch (err: any) {
        error('Error inesperado al insertar')

    } finally {
        isProcessing.value = false
    }

    // Confirmación de inserción
    const result = await question('Se va a insertar el registro.', '¿Deseas insertar este grupo?');
    if (!result.isConfirmed) return;

    const dataCabecera = { model: "scgcata", 
                            data: { cuenta: formData.value.cuenta, 
                                    descripcion: formData.value.descripcion,
                                    creado_por: userStore.globalUser, 
                                    fecha_creado: dateTimeStore.formattedDate, 
                                    hora_creado: dateTimeStore.formattedTime,
                                    naturaleza: formData.value.naturaleza,
                                    nivel_cuenta: formData.value.nivel_cuenta,
                                    tipo_cuenta: formData.value.tipo_cuenta,
                                    grupo_cuenta: formData.value.grupo_cuenta,
                                    recibe: formData.value.recibe,
                                    aux_interno: formData.value.aux_interno,
                                    aux_externo: formData.value.aux_externo,
                                    status: formData.value.status }}
    try {
        const responseCab = await fetch(dUrl.urlGlobal + '/api3/insert/', { 
                                method: 'POST', 
                                headers: { 'Content-Type': 'application/json' }, 
                                body: JSON.stringify(dataCabecera)})

        if (!responseCab.ok) { 
            error('Error al insertar cabecera'); 
            return }

        success('Datos insertados correctamente', 'Inserción exitosa');
        mode.value = 'view';
        resetAll(); // Limpiamos los campos
    } catch (err: any) {
        error('Error inesperado al insertar')

    } finally {
        isProcessing.value = false
    }
}

// Función para manejar la actualización de la cabecera y los detalles
const handleUpdate = async () => {
    if (isProcessing.value) return;
    isProcessing.value = true;

    const result = await question('Se va a actualizar el registro.', '¿Deseas actualizarlo?');
    if (!result.isConfirmed) return;

    try {
        const responseCab = await axios.post(dUrl.urlGlobal + '/api3/update/', {
            table: 'scgcata',
            filters: { cuenta: formData.value.cuenta },
            data: {
                cuenta: formData.value.cuenta,
                descripcion: formData.value.descripcion,
                naturaleza: formData.value.naturaleza,
                nivel_cuenta: formData.value.nivel_cuenta,
                tipo_cuenta: formData.value.tipo_cuenta,
                grupo_cuenta: formData.value.grupo_cuenta,
                recibe: formData.value.recibe,
                aux_interno: formData.value.aux_interno,
                aux_externo: formData.value.aux_externo,
                status: formData.value.status,
                modificado_por: userStore.globalUser,
                fecha_status: dateTimeStore.formattedDate,
                hora_status: dateTimeStore.formattedTime
            }
        });

        if (responseCab.status !== 200) {
            error('Error actualizando cabecera');
            return;
        }

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

    try {
        const response = await axios.get(`${dUrl.urlGlobal}/api3/scgcata/valida?id_cuenta=${formData.value.cuenta}`);

        const tablas = response.data;
        if (tablas) {
            for ( let i = 0; i < tablas.length; i++) {
                if (tablas[i] === 'scgafed') {
                    error('Cuenta no puede eliminarse, hay registros en afectaciones generadas')
                }
                if (tablas[i] === 'scgascta') {
                    error('Cuenta no puede eliminarse, hay registros en Asientos Contables')
                }
                if (tablas[i] === 'scglisc') {
                    error('Cuenta no puede eliminarse, hay registros en Parámetros Afectaciones')
                }
                if (tablas[i] === 'scgmayd') {
                    error('Cuenta no puede eliminarse, hay registros en Detalles del Mayor')
                }
                if (tablas[i] === 'scghide') {
                    error('Cuenta no puede eliminarse, hay registros en Histórico de Cuentas')
                }
            }
            return
        }
    }
    catch (err: any) {
        error('Error inesperado al insertar')

    } finally {
        isProcessing.value = false
    }

    const resultado = await question(`Se va a eliminar la Cuenta ${formData.value.cuenta}`, '¿Deseas eliminarla?');
    if (!resultado.isConfirmed) return;

    try {
        const response = await axios.post(dUrl.urlGlobal + '/api3/delete/', {
            table: 'scgcata',
            filters: { cuenta: formData.value.cuenta } });

        if (response.status !== 200) {
            error('Error al eliminar el registro');
            return;
        }

        success(`Se eliminó la Cuenta ${formData.value.cuenta}`, 'Evento exitoso')

        mode.value = 'search';
    } catch (err: any) {
        error(err.response?.data?.detail || 'Error inesperado');
    } finally {
        isProcessing.value = false
    }
};
// ================= BÚSQUEDA =================
const handleSearch = async () => {
    if (isProcessing.value) return;
    isProcessing.value = true;

    try {
        // Realizamos la búsqueda a la API
        const response = await axios.post(dUrl.urlGlobal + '/api3/query', 
                        { tabla: 'scgcata', 
                            filtro: { cuenta: formData.value.cuenta,
                                        descripcion: formData.value.descripcion,
                                        naturaleza: formData.value.naturaleza,
                                        nivel_cuenta: formData.value.nivel_cuenta,
                                        tipo_cuenta: formData.value.tipo_cuenta,
                                        grupo_cuenta: formData.value.grupo_cuenta,
                                        recibe: formData.value.recibe,
                                        aux_interno: formData.value.aux_interno,
                                        aux_externo: formData.value.aux_externo,
                                        status: formData.value.status} });
        // Guardamos los datos obtenidos en dataList
    
        dataList.value = response.data;

        // Establecemos el índice actual en 0
        currentIndex.value = 0;

        // Si hay datos, actualizamos el formulario y detalles
        if (dataList.value.length > 0) {
            updateFormData(); // Actualiza el formulario y detalles con el primer registro
            canNavigate.value = true;
            //mode.value = 'view'
        } else {
            warning('No se encontraron registros', '');
            canNavigate.value = false;
        }
    } catch (err: any) {
        error('Error al realizar la búsqueda');
    } finally {
        isProcessing.value = false
    }
};
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
        case 'search':
            await handleSearch();
            break;
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
    formData.value = {
        cuenta: '',
        descripcion: '',
        naturaleza: '',
        nom_naturaleza: '',
        nivel_cuenta: '',
        tipo_cuenta: '',
        nom_tipo: '',
        grupo_cuenta: '',
        nom_grupo: '',
        recibe: '',
        aux_interno: '',
        aux_externo: '',
        status: 'A',
        nom_status: 'Activo'
    };
    canNavigate.value = false;
};

onMounted(async() => {
    try {
        scggcta.value = (await axios .get(`${dUrl.urlGlobal}/api3/scggcta`)).data;
    } catch (err: any) {
        error('Error al cargar datos iniciales');
    }
    
    try {
        scgsgcta.value = (await axios .get(`${dUrl.urlGlobal}/api3/scgsgcta`)).data;
    } catch (err: any) {
        error('Error al cargar datos iniciales');
    }
  
  try {
        scgcodi.value = (await axios .get(`${dUrl.urlGlobal}/api3/scgcodi`)).data;
    } catch (err: any) {
        error('Error al cargar datos iniciales');
    }
});

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

.glass-wrapper {
    font-family: 'Poppins', sans-serif;
    padding: 25px;
    background: rgba(255, 255, 255, 0.55);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    gap: 22px;
}

/* ================= HEADER ================= */
.top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.title {
    font-size: 18px;
    font-weight: 600;
}

.action-group {
    display: flex;
    gap: 10px;
}

/* ================= BUTTONS ================= */
.action-btn {
    padding: 7px 16px;
    border-radius: 14px;
    border: none;
    cursor: pointer;
    font-size: 13px;
    font-weight: 500;
    transition: all 0.25s ease;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}

.action-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.08);
}

.action-btn.active {
    border: 2px solid currentColor;
    box-shadow: 0 0 12px rgba(0, 0, 0, 0.15);
    transform: scale(1.05);
}

/* Insert */
.action-btn.insert {
    background: rgba(93, 116, 183, 0.15);
    color: #3f5fa8;
}

/* Search */
.action-btn.search {
    background: rgba(0, 123, 255, 0.15);
    color: #007bff;
}

/* Update */
.action-btn.update {
    background: rgba(188, 211, 74, 0.25);
    color: #7a941a;
}

/* Delete */
.action-btn.delete {
    background: rgba(217, 75, 106, 0.18);
    color: #c23c5d;
}

/* Confirm / Cancel */
.action-btn.confirm {
    background: rgba(40, 167, 69, 0.2);
    color: #28a745;
}

.action-btn.cancel {
    background: rgba(108, 117, 125, 0.2);
    color: #6c757d;
}

/* ================= FORM ================= */
.form-card {
    padding: 18px;
    border-radius: 16px;
    background: rgba(255, 255, 255, 0.65);
    backdrop-filter: blur(14px);
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.form-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px;
}

input,
select {
    width: 100%;
    padding: 6px;
    border-radius: 6px;
    border: 1px solid rgba(0, 0, 0, 0.1);
    font-size: 13px;
}

/* ================= DETALLE TABLE ================= */
.detalle-table {
    max-height: 240px;
    overflow-y: auto;
    border-radius: 16px;
    background: rgba(255, 255, 255, 0.55);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.75);
}

.detalle-table table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
}

.detalle-table th {
    background: rgba(255, 255, 255, 0.75);
    position: sticky;
    top: 0;
    backdrop-filter: blur(10px);
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
    color: #666;
    letter-spacing: 0.4px;
}

.detalle-table td {
    padding: 6px 8px;
    border-top: 1px solid rgba(0, 0, 0, 0.05);
    color: #444;
    text-align: center;
}

.detalle-table tbody tr {
    transition: all 0.25s ease;
    cursor: pointer;
}

.detalle-table tbody tr:hover {
    background: rgba(255, 255, 255, 0.8);
    transform: scale(1.002);
}

/* ================= FOOTER ================= */
.footer-actions {
    display: flex;
    justify-content: flex-end;
    gap: 0.8rem;
    margin-top: 1rem;
}

.footer-navigation {
    display: flex;
    justify-content: center;
    gap: 0.8rem;
    margin-top: 1rem;
}

.footer-navigation button {
    min-width: 75px;
    padding: 6px 14px;
    border-radius: 12px;
    border: none;
    cursor: pointer;
    font-size: 13px;
    font-weight: 500;
    transition: all 0.25s ease;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}

.footer-navigation button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.08);
}

.table-header-actions {
    display: flex;
    justify-content: end;
    padding: 8px;
}

.detalle-table table {
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed;
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
