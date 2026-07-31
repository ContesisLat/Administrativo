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
                    <label for="tercero">Tercero</label>
                    <input type="string" id="tercero" v-model="formData.tercero" :readonly="mode === 'view'" required />
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
                    <label for="tipo_interno">Tipo Cuenta</label>
                        <select id="tipo_interno" v-model="formData.tipo_interno" :disabled="mode === 'view'" required>
                            <option value="1">Persona Natural</option>
                            <option value="2">Persona Jurídica</option>
                            <option value="3">Equipo Rodante</option>
                            <option value="4">Departamento</option>
                            <option value="9">Otros</option>
                    </select>
                </div>
                <div>
                    <label for="no_cedula">Cédula</label>
                    <input type="string" id="no_cedula" v-model="formData.no_cedula" :readonly="mode === 'view'" required/>
                </div>
            </div>
            <div class="form-grid"> 
                <div>
                    <label for="no_ruc">Ruc</label>
                    <input type="string" id="no_ruc" v-model="formData.no_ruc" :readonly="mode === 'view'" required/>
                         
                </div>
                <div>
                    <label for="digito verificador">DV</label>
                    <input type="number" id="digito_verificador" v-model="formData.digito_verificador" :readonly="mode === 'view'" required/>
                </div>
                <div> 
                    <label for="no_placa">No. Placa</label>
                    <input type="string" id="no_placa" v-model="formData.no_placa" :readonly="mode === 'view'" required/> 
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
import { Scgterc } from '@/interface/interfaces';

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
    document.getElementById("tercero")?.focus();
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
    tercero: '',
    descripcion: '',
    tipo_interno: '',
    no_cedula: '',
    no_ruc: '',
    digito_verificador: 0,
    no_placa: '',
    status: 'A',
    nom_status: 'Activo'
});

const scgterc = ref<Scgterc[]>([]);

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

    if (!formData.value.tercero || !formData.value.descripcion ||
        !formData.value.tipo_interno || !formData.value.status) {
        error('Complete todos los campos obligatorios');
        isProcessing.value = false;
        return; 
    }
    if (formData.value.tipo_interno == '1' && (!formData.value.no_cedula ||
        formData.value.no_placa && formData.value.no_ruc && formData.value.digito_verificador)) {
        error('Para Persona Natural solo debe registrar la cédula...')
        isProcessing.value = false;
        return;
    }
    if (formData.value.tipo_interno == '2' && !formData.value.no_ruc || !formData.value.digito_verificador) {
        error('Para Persona Jurídica debe registrar el Ruc y el DV...')
        isProcessing.value = false;
        return;
    }
    if (formData.value.tipo_interno == '2' && (formData.value.no_cedula || formData.value.no_placa )) {
        error('Para Persona Jurídica solo debe registrar Ruc ni DV...')
        isProcessing.value = false;
        return;
    }
     
    if (formData.value.tipo_interno == '3' && (!formData.value.no_placa &&
        formData.value.no_cedula || formData.value.no_ruc || formData.value.digito_verificador)) { 
        error('Para Equipo Rodante tiene que registrar la placa...')
        isProcessing.value = false;
        return;
    }

    try {
        const response = await axios.post(dUrl.urlGlobal + '/api3/query', { tabla: 'scgterc', filtro: { cuenta: formData.value.tercero}});
        const existe = response.data.length > 0;
        if (existe) {
            error('Código de Tercero ya existe...')
            return
        }
    }
    catch (err: any) {
        error('Error inesperado al insertar')

    } finally {
        isProcessing.value = false
    }

    // Confirmación de inserción
    const result = await question('Se va a insertar el Tercero.', '¿Deseas ingresarlo?');
    if (!result.isConfirmed) return;

    const dataCabecera = { model: "scgterc", 
                            data: { tercero: formData.value.tercero, 
                                    descripcion: formData.value.descripcion,
                                    creado_por: userStore.globalUser, 
                                    fecha_creado: dateTimeStore.formattedDate, 
                                    hora_creado: dateTimeStore.formattedTime,
                                    tipo_interno: formData.value.tipo_interno,
                                    no_cedula: formData.value.no_cedula,
                                    no_ruc: formData.value.no_ruc,
                                    digito_verificador: formData.value.digito_verificador,
                                    no_placa: formData.value.no_placa,
                                    status: formData.value.status }}
    try {
        const responseCab = await fetch(dUrl.urlGlobal + '/api3/insert/', { 
                                method: 'POST', 
                                headers: { 'Content-Type': 'application/json' }, 
                                body: JSON.stringify(dataCabecera)})

        if (!responseCab.ok) { 
            error('Error al insertar el registro'); 
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
            table: 'scgterc',
            filters: { tercero: formData.value.tercero },
            data: {
                tercero: formData.value.tercero,
                descripcion: formData.value.descripcion,
                tipo_interno: formData.value.tipo_interno,
                no_cedula: formData.value.no_cedula,
                no_ruc: formData.value.no_ruc,
                digito_verificador: formData.value.digito_verificador,
                no_placa: formData.value.no_placa,
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
        const response = await axios.get(`${dUrl.urlGlobal}/api3/scgterc/valida?id_tercero=${formData.value.tercero}`);

        const tablas = response.data;
        if (tablas) {
            for ( let i = 0; i < tablas.length; i++) {
                if (tablas[i] === 'scgafed') {
                    error('Tercero no puede eliminarse, hay registros en afectaciones generadas')
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

    const resultado = await question(`Se va a eliminar el Tercero ${formData.value.tercero}`, '¿Deseas eliminarla?');
    if (!resultado.isConfirmed) return;

    try {
        const response = await axios.post(dUrl.urlGlobal + '/api3/delete/', {
            table: 'scgterc',
            filters: { cuenta: formData.value.tercero } });

        if (response.status !== 200) {
            error('Error al eliminar el registro');
            return;
        }

        success(`Se eliminó el Tercero ${formData.value.tercero}`, 'Evento exitoso')

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
                        { tabla: 'scgterc', 
                            filtro: { tercero: formData.value.tercero,
                                        descripcion: formData.value.descripcion,
                                        tipo_interno: formData.value.tipo_interno,
                                        no_cedula: formData.value.no_cedula,
                                        no_ruc: formData.value.no_ruc,
                                        digito_verificador: formData.value.digito_verificador,
                                        no_placa: formData.value.no_placa,
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
        tercero: '',
        descripcion: '',
        tipo_interno: '',
        no_cedula: '',
        no_ruc: '',
        digito_verificador: 0,
        no_placa: '',
        status: 'A',
        nom_status: 'Activo'
    };
    canNavigate.value = false;
};
 
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
