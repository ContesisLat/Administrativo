<template>
    <div class="glass-wrapper">
        <!-- ================= HEADER ================= -->
        <div class="top-bar">
            <div class="title">Servicios a Aeronaves</div>
            <div class="action-group">
                <button class="action-btn insert" @click="setMode('insert')" :disabled="!canInsert"
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
                    <label for="fecha">Fecha</label>
                    <input type="date" id="fecha" v-model="formData.fecha" :readonly="mode === 'view'" required />
                </div>
                <div>
                    <label for="status">Estado</label>
                    <select id="status" v-model="formData.status" :disabled="mode === 'view'" required>
                        <option value="R">Registrado</option>
                        <option value="F">Facturado</option>
                        <option value="C">Cerrado</option>
                        <option value="A">Anulado</option>
                    </select>
                </div>
                <div>
                    <label for="compania">Compañía</label>
                    <select id="compania" v-model="formData.compania" :disabled="mode === 'view'" required>
                        <option v-for="i in companias" :key="i.compania" :value="i.compania">
                            {{ i.nombre }}
                        </option>
                    </select>
                </div>
                <div>
                    <label for="matricula">Matrícula</label>
                    <input id="matricula" v-model="formData.matricula" :readonly="mode === 'view'" required />
                </div>
                <div>
                    <label for="aeronave">Tipo Aeronave</label>
                    <select id="aeronave" v-model="formData.aeronave" :disabled="mode === 'view'" required>
                        <option v-for="i in aeronaves" :key="i.aeronave" :value="i.aeronave">
                            {{ i.descripcion }}
                        </option>
                    </select>
                </div>
                <div>
                    <label for="fecha_llegada">Fecha Llegada</label>
                    <input type="date" id="fecha_llegada" v-model="formData.fecha_llegada" :readonly="mode === 'view'"
                        required />
                </div>
                <div>
                    <label for="hora_llegada">Hora Llegada</label>
                    <input type="time" id="hora_llegada" v-model="formData.hora_llegada" :readonly="mode === 'view'"
                        required />
                </div>
                <div>
                    <label for="monto_servicio">Monto Servicio</label>
                    <input id="monto_servicio" v-model="formData.monto_servicio" readonly />
                </div>
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
                        <th class="resizable">Cargo <span class="resizer" @mousedown="startResize($event)"
                                aria-label="Redimensionar columna"></span></th>
                        <th class="resizable">Tiempo Total <span class="resizer" @mousedown="startResize($event)"
                                aria-label="Redimensionar columna"></span></th>
                        <th class="resizable">Monto <span class="resizer" @mousedown="startResize($event)"
                                aria-label="Redimensionar columna"></span></th>
                        <th class="resizable">Estado <span class="resizer" @mousedown="startResize($event)"
                                aria-label="Redimensionar columna"></span></th>
                        <th v-if="mode === 'insert'">Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(fila, index) in registros" :key="index">
                        <td>
                            <select v-model="fila.cargo" :disabled="mode === 'view'" required>
                                <option v-for="c in cargos" :key="c.cargo" :value="c.cargo">
                                    {{ c.nombre }}
                                </option>
                            </select>
                        </td>
                        <td>
                            <input v-model="fila.tiempo_total" :readonly="mode === 'view'" @blur="Calcular(index)"
                                required />
                        </td>
                        <td>
                            <input v-model="fila.monto" readonly />
                        </td>
                        <td>
                            <select v-model="fila.status" :disabled="mode === 'view'" required>
                                <option value="R">Registrado</option>
                                <option value="I">Inactivo</option>
                            </select>
                        </td>
                        <td v-if="mode === 'insert'">
                            <button class="action-btn delete" @click="removeRow(index)" aria-label="Eliminar Fila">
                                X
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
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

// Función para cambiar el modo
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
    fecha: '',
    compania: '',
    matricula: '',
    aeronave: '',
    fecha_llegada: '',
    hora_llegada: '',
    monto_servicio: 0,
    factura: '',
    status: 'R',
});

interface Registro {
    cargo: string;
    tiempo_total: string;
    monto: string;
    status: string;
}

const registros = ref<Registro[]>([]);
const companias = ref<any[]>([]);
const aeronaves = ref<any[]>([]);
const cargos = ref<any[]>([]);

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

// Función para obtener los detalles de la API
const getCaratvued = ref<any[]>([]);
const getCaratvue = async () => {
    // Limpiamos las listas antes de hacer la búsqueda
    registros.value = [];

    try {
        // Realizamos la solicitud a la API con los filtros de búsqueda
        const response = await axios.get(
            `https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api2/caratvued/filter?fecha=${formData.value.fecha}&compania=${formData.value.compania}&matricula=${formData.value.matricula}`
        );

        // Asignamos los datos a getCaratvued y a registros
        getCaratvued.value = response.data; // Cargamos los datos en getCaratvued

        // Mapeamos los datos obtenidos para ajustarlos al formato de registros
        registros.value = getCaratvued.value.map((i: any) => ({
            cargo: i.cargo || '',
            tiempo_total: i.tiempo_total || '',
            monto: i.monto || null,
            status: i.status || '',
            nom_status: i.nom_status || ''
        }));

    } catch (err) {
        error('Hubo un error al obtener los detalles');
    }
};

// ================= NAVEGACIÓN ENTRE REGISTROS =================
function prevRecord() {
    if (currentIndex.value > 0) {
        currentIndex.value--;
        updateFormData();  // Actualizamos los datos al navegar
        getCaratvue()
    }
}

function nextRecord() {
    if (currentIndex.value < dataList.value.length - 1) {
        currentIndex.value++;
        updateFormData();  // Actualizamos los datos al navegar
        getCaratvue()
    }
}

// ================= CALCULAR =================
async function Calcular(index: number) {
    const row = registros.value[index];
    if (!row?.cargo) return;

    const patronHora = /^([0-9]{1,2}):([0-5][0-9])$/;
    if (!patronHora.test(row.tiempo_total)) {
        error('Formato hora inválido');
        return;
    }

    try {
        const response = await axios.get(
            `https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api2/cartarvue/tarifas?id_aeronave=${formData.value.aeronave}&id_fecha=${formData.value.fecha}&id_cargo=${row.cargo}&id_tiempo=${row.tiempo_total}`
        );
        row.monto = response.data[0]?.costo_hora || '0';
        recalcularTotal(); // Recalcular el monto del servicio total
    } catch (err: any) {
        error('Error al calcular monto del servicio');
    }
}


/* ================= CRUD ================= */
// Función para validar que no haya cargos repetidos
function valida(arr: string[]): boolean { return new Set(arr).size === arr.length }

// Función para manejar la inserción
async function handleInsert() {
    if (isProcessing.value) return;
    isProcessing.value = true;

    if (!formData.value.fecha || !formData.value.compania || !formData.value.matricula || !formData.value.aeronave || !formData.value.fecha_llegada || !formData.value.hora_llegada) {
        error('Complete todos los campos obligatorios');
        return;
    }

    if (formData.value.fecha_llegada > formData.value.fecha) {
        error('La fecha de llegada no puede ser posterior a la fecha del servicio');
        return;
    }

    const detallesActivos = registros.value.filter(r => r.status !== 'I');
    if (detallesActivos.length === 0) {
        error('Por favor, ingrese al menos un detalle de servicio');
        return;
    }

    if (!valida(detallesActivos.map(r => r.cargo))) {
        error('Existen cargos repetidos en el servicio');
        return;
    }

    // Confirmación de inserción
    const result = await question('Se va a insertar el registro.', '¿Deseas insertar este registro?');
    if (!result.isConfirmed) return;

    const dataCabecera = { model: "caratvue", data: { ...formData.value, creado_por: userStore.globalUser, fecha_creado: dateTimeStore.formattedDate, hora_creado: dateTimeStore.formattedTime } }
    try {
        const responseCab = await fetch('https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api2/insert/', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(dataCabecera) })
        if (!responseCab.ok) { error('Error al insertar cabecera'); return }

        // Insertamos los detalles
        for (const fila of detallesActivos) {
            const dataDetalle = { model: "caratvued", data: { ...fila, ...formData.value, creado_por: userStore.globalUser, fecha_creado: dateTimeStore.formattedDate, hora_creado: dateTimeStore.formattedTime } }
            await fetch('https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api2/insert/', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(dataDetalle) })
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
const upsertDetalle = async (fila: { cargo: string; tiempo_total: any; monto: any; status: any }) => {
    if (!fila.cargo) return;
    try {
        const response = await axios.post('https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api2/query', { tabla: 'caratvued', filtro: { fecha: formData.value.fecha, compania: formData.value.compania, matricula: formData.value.matricula, cargo: fila.cargo } });
        const existe = response.data.length > 0;
        if (!existe) {
            const dataInsert = { tabla: 'caratvued', data: { ...fila, ...formData.value, creado_por: userStore.globalUser, fecha_creado: dateTimeStore.formattedDate, hora_creado: dateTimeStore.formattedTime } };
            const resInsert = await fetch('https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api2/insert/', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(dataInsert) });
            if (!resInsert.ok) error(`Error insertando cargo ${fila.cargo}`);
        } else {
            const dataUpdate = {
                table: 'caratvued',
                filters: {
                    fecha: formData.value.fecha,
                    compania: formData.value.compania,
                    matricula: formData.value.matricula,
                    cargo: fila.cargo
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

            const resUpdate = await axios.post('https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api2/update/', dataUpdate);
            if (resUpdate.status !== 200) error(`Error actualizando cargo ${fila.cargo}`);
        }
    } catch (err: any) {
        error(err.response?.data?.detail || `Error procesando cargo ${fila.cargo}`);
    }
};

// Función para manejar la actualización de la cabecera y los detalles
const handleUpdate = async () => {
    if (isProcessing.value) return;
    isProcessing.value = true;

    const result = await question('Se va a actualizar el registro.', '¿Deseas actualizar este registro?');
    if (!result.isConfirmed) return;

    try {
        const responseCab = await axios.post('https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api2/update/', {
            table: 'caratvue',
            filters: { fecha: formData.value.fecha, compania: formData.value.compania, matricula: formData.value.matricula },
            data: {
                ...formData.value,
                modificado_por: userStore.globalUser,
                fecha_status: dateTimeStore.formattedDate,
                hora_status: dateTimeStore.formattedTime
            }
        });

        if (responseCab.status !== 200) {
            error('Error actualizando cabecera');
            return;
        }

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
        const response = await axios.post('https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api2/update/', {
            table: 'caratvue',
            filters: { fecha: formData.value.fecha, compania: formData.value.compania, matricula: formData.value.matricula },
            data: { status: 'I' }
        });

        if (response.status !== 200) {
            error('Error al inactivar registro');
            return;
        }

        // Inactivar los detalles de los registros
        for (const fila of registros.value) {
            if (!fila.cargo) continue;
            try {
                await axios.post('https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api2/update/', {
                    table: 'caratvued',
                    filters: { fecha: formData.value.fecha, compania: formData.value.compania, matricula: formData.value.matricula, cargo: fila.cargo },
                    data: { status: 'I' }
                });
            } catch (err: any) {
                console.log(err);
            }
        }

        success('Registro y detalles inactivados correctamente', 'Acción exitosa');
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
        const response = await axios.post('https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api2/query', { tabla: 'caratvue', filtro: formData.value });

        // Guardamos los datos obtenidos en dataList
        dataList.value = response.data;

        // Establecemos el índice actual en 0
        currentIndex.value = 0;

        // Si hay datos, actualizamos el formulario y detalles
        if (dataList.value.length > 0) {
            updateFormData(); // Actualiza el formulario y detalles con el primer registro
            canNavigate.value = true;
            getCaratvue()
        } else {
            warning('No se encontraron registros', '');
            canNavigate.value = false;
            registros.value = []; // Limpiamos los detalles si no hay resultados
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
    registros.value = [];
    formData.value = {
        fecha: '',
        compania: '',
        matricula: '',
        aeronave: '',
        fecha_llegada: '',
        hora_llegada: '',
        monto_servicio: 0,
        factura: '',
        status: 'R',
    };
    canNavigate.value = false;
};

// ================= AGREGAR / ELIMINAR FILAS =================
function addRow() {
    registros.value.push({
        cargo: '',
        tiempo_total: '',
        monto: '0',
        status: 'R'
    });
}

function removeRow(index: number) {
    registros.value.splice(index, 1);
    recalcularTotal(); // Recalcular el total del servicio
}

function recalcularTotal() {
    formData.value.monto_servicio = registros.value.reduce(
        (sum, r) => r.status !== 'I'
            ? sum + parseFloat(r.monto || '0')
            : sum,
        0
    );
}

/* ================= RESIZE COLUMNAS ================= */

let currentTh: HTMLElement | null = null
let startX = 0
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

onMounted(async () => {
    try {
        companias.value = (await axios.get('https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api2/compania/filter?status=A')).data;
        aeronaves.value = (await axios.get('https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api2/cartiaero/')).data;
        cargos.value = (await axios.get('https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api2/caratenvue/filter?status=A')).data;
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
