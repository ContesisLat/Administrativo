<template>
    <div class="glass-wrapper">
        <!-- ================= HEADER ================= -->
        <div class="top-bar">
            <div class="title">Categorías de Gerencias y Deptos</div>
            <div class="action-group">
                <button class="action-btn insert" @click="setMode('insert'); addRowEnc" | v-on:click="focusInput()" :disabled="!canInsert"
                    :class="{ active: mode === 'insert' }">
                    Insertar
                </button>

                <!--button class="action-btn search" @click="setMode('search')" :disabled="!canSearch"
                    :class="{ active: mode === 'search' }">
                    Buscar
                </button-->

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
                <button @click="prevRecord" :disabled="currentIndexEnc === 0 || isViewMode"
                    aria-label="Registro Anterior">Anterior</button>
                <button @click="nextRecord" :disabled="currentIndexEnc === dataList.length - 1 || isViewMode"
                    aria-label="Registro Siguiente">Siguiente</button>
            </div>
        </div>

        <!-- ================= Encabezado ================= -->
        <div class="detalle-table">
            <div class="table-header-actions">
                <button v-if="mode === 'insert'" class="action-btn insert" @click="addRowEnc" | v-on:click="focoHijo()" aria-label="Agregar Fila">
                    + Agregar Fila
                </button>
            </div>
            <table>
                <thead>
                    <tr>
                        <th class="resizable">Gerencia<span class="resizer" @mousedown="startResize($event)"
                                aria-label="Redimensionar columna"></span></th>
                        <th class="resizable">Descripción <span class="resizer" @mousedown="startResize($event)"
                                aria-label="Redimensionar columna"></span></th>
                        <th class="resizable">Estado <span class="resizer" @mousedown="startResize($event)"
                                aria-label="Redimensionar columna"></span></th>
                        <th v-if="mode === 'insert'">Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(filaEnc, indexE) in registroEnc"  :key="indexE">
                        <td>
                           <input v-model="filaEnc.gerencia" :readonly="mode === 'view'" required />
                        </td>
                        <td>
                            <input v-model="filaEnc.descripcion" :readonly="mode === 'view'" required />
                        </td>
                        <td>
                            <select v-model="filaEnc.status" :readonly="mode === 'view'" required>
                                <option value="A">Activo</option>
                                <option value="I">Inactivo</option>
                            </select>
                        </td>
                        <td v-if="mode === 'insert'">
                            <button class="action-btn delete" @click="removeRowEnc(indexE)" aria-label="Eliminar Fila">
                                X
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- ================= DETALLE ================= -->
        <div class="detalle-table">
            <div class="table-header-actions">
                <button v-if="mode === 'insert' || 'edit'" class="action-btn insert" @click="addRow" | v-on:click="focoHijo()" aria-label="Agregar Fila">
                    + Agregar Fila
                </button>
            </div>
            <table>
                <thead>
                    <tr>
                        <th class="resizable">Departamento<span class="resizer" @mousedown="startResize($event)"
                                aria-label="Redimensionar columna"></span>
                        </th>
                        <th class="resizable">Descripción <span class="resizer" @mousedown="startResize($event)"
                                aria-label="Redimensionar columna"></span>
                        </th>
                        <th class="resizable">T. Aplica <span class="resizer" @mousedown="startResize($event)"
                            aria-label="Redimensionar columna"></span>  
                        </th>
                        <th class="resizable">Clase <span class="resizer" @mousedown="startResize($event)"
                                aria-label="Redimiensionar columna"></span>
                        </th>
                        <th class="resizable">SubClase <span class="resizer" @mousedown="startResize($event)"
                                aria-label="Redimensionar columna"></span>  
                        </th>
                        <th class="resizable">Estado <span class="resizer" @mousedown="startResize($event)"
                                aria-label="Redimensionar columna"></span></th>
                        <th v-if="mode === 'insert'">Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(fila, index) in registros" @click="cargaLinea(index)"  :key="index">
                        <td>
                           <input v-model="fila.departamento" :readonly="mode === 'view'" required />  
                        </td>
                        <td>
                            <input v-model="fila.descripcion" :readonly="mode === 'view'" required />
                        </td>
                        <td>
                            <select id="scgtapl" v-model="fila.tipo_aplica" :readonly="mode === 'view'" required>
                                <option v-for="i in scgtapl" :key="i.tipo_aplica" :value="i.tipo_aplica">
                                    {{ i.descripcion }}
                                </option>
                            </select>
                        </td>
                        <td> 
                            <select id="scgclas" v-model="fila.clase" :readonly="mode === 'view'" required> 
                                <option v-for="i in scgclas" :key="i.clase" :value="i.clase">
                                    {{ i.descripcion }}
                                </option>
                            </select>
                        </td>
                        <td>             
                            <select id="scgscla" v-model="fila.subclase" :readonly="mode === 'view'" required>
                                <option v-for="k in scgscla" :key="k.subclase" :value="k.subclase ">
                                    {{ k.descripcion }}
                                </option>
                            </select>
                        </td>
                        <td> 
                            <select v-model="fila.status" :disabled="mode === 'view'" required>
                                <option value="A">Activo</option>
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
import { Seggere, Segdept, Scgdept, Scgclas, Scgscla, Scgtapl} from '@/interface/interfaces';

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
        //(mode.value === 'search' && dataList.value.length > 0 )
        (mode.value === 'search' && registroEnc.value.length > 0 ) ||
        (mode.value === 'view' && registroEnc.value.length > 0)
    ) && !isProcessing.value
);

const canDelete = computed(() =>
    (
        (mode.value === 'view' && canNavigate.value) ||
        (mode.value === 'search' && dataList.value.length > 0)
    ) && !isProcessing.value
);

function cargalineaEnc(nlinea: number) {
    let ArrayEnc = nlinea
}

function cargaLinea(nlinea: number) {
    let lineaArray = nlinea
}
// Función para cambiar el modo
function focusInput() {
    document.getElementById("gerencia")?.focus();
}

function focoHijo() {
    let cantidad = registros.value.length
    
    console.log(cantidad)
    cantidad--
     
    console.log(cantidad)

    document.getElementById(`transaccion[${cantidad}]`)?.focus();
}

function setMode(newMode: Mode) {
    if (isProcessing.value) return;

    switch (mode.value) {

        case 'view':
            if (newMode === 'insert' || newMode === 'edit' || newMode === 'search') {
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
interface RegistroEnc {
    compania: '',
    gerencia: '',
    descripcion: '',
    status: 'A',
    nom_status: 'Activo'
}

interface Registro {
    departamento: string,
    descripcion: string,
    tipo_aplica: string,
    clase: string,
    subclase: string,
    status: string,
    nom_status: string
}

const registroEnc = ref<RegistroEnc[]>([]);
const registros = ref<Registro[]>([]);
const seggere = ref<Seggere[]>([]);
const segdept = ref<Segdept[]>([]);
const scgclas = ref<Scgclas[]>([]);
const scgscla = ref<Scgscla[]>([]);
const scgtapl = ref<Scgtapl[]>([])
const scgdept = ref<Scgdept[]>([]);
 
// ================= NAVEGACIÓN =================
const dataList = ref<any[]>([]);
const currentIndex = ref(0);
const currentIndexEnc = ref(0);
const canNavigate = ref(false);

// Actualiza los datos del formulario y los detalles
function updateFormData() {
    const record = dataList.value[currentIndex.value];
    if (!record) return;

    // Llenamos el formulario con la cabecera del registro
    registroEnc.value = { ...record };

}
// Función para obtener los detalles de la API
const getSegdept = ref<any[]>([]);
const getSeggere = async () => {
    // Limpiamos las listas antes de hacer la búsqueda
    registros.value = [];
    const filaE = registroEnc.value[currentIndexEnc.value];

    try {
        // Realizamos la solicitud a la API con los filtros de búsqueda
        const response = await axios.get(
            `${dUrl.urlGlobal}/api3/segdept/filter?gerencia=${filaE.gerencia}`
        );

        // Asignamos los datos a getCaratvued y a registros
        getSegdept.value = response.data; // Cargamos los datos en getCaratvued

        // Mapeamos los datos obtenidos para ajustarlos al formato de registros
        registros.value = getSegdept.value.map((i: any) => ({
            departamento: i.departamento || '',
            descripcion: i.descripcion || '',
            tipo_aplica: i.tipo_aplica || '',
            clase: i.clase || '',
            subclase: i.subclase || '',
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
        getSeggere()
    }
}

function nextRecord() {
    if (currentIndex.value < dataList.value.length - 1) {
        currentIndex.value++;
        updateFormData();  // Actualizamos los datos al navegar
        getSeggere()
    }
}

// Función para validar que no haya cargos repetidos
function valida(arr: string[]): boolean { return new Set(arr).size === arr.length }

// Función para manejar la inserción
async function handleInsert() {
    if (isProcessing.value) return;
    isProcessing.value = true;
    let fila = registroEnc.value.length
    const filaE = registroEnc.value[fila]
    
    console.log(currentIndexEnc.value)
    console.log(filaE)

    if (!filaE.gerencia || !filaE.descripcion || !filaE.status) {
        error('Complete todos los campos obligatorios');
        return;
    }

    try {
        const response = await axios.post(dUrl.urlGlobal + '/api3/querytpy/', { tabla: 'seggere', 
                                                                    filtro: { compania: '010', gerencia: filaE.gerencia}});
        const existe = response.data.length > 0;
        if (!existe) {
            error('Gerencia ya existe...')
            return
        }
    }
    catch (err: any) {
        error('Error inesperado al insertar')

    } finally {
        isProcessing.value = false
    }

    const detallesActivos = registros.value.filter(r => r.status !== 'I');
    
    if (detallesActivos.length === 0) {
        error('Por favor, ingrese al menos un detalle de las Gerencias');
        return;
    }

    if (!valida(detallesActivos.map(r => r.departamento))) {
        error('Existen grupos repetidos');
        return;
    }

    // Confirmación de inserción
    const result = await question('Se va a insertar el registro.', '¿Deseas insertar esta Gerencia?');
    if (!result.isConfirmed) return;

    const dataCabecera =  { model: 'seggere', data: { compania: '010',
                                                        gerencia: filaE.gerencia, 
                                                        descripcion: filaE.descripcion,
                                                        status: filaE.status, 
                                                        creado_por: userStore.globalUser, 
                                                        fecha_creacion: dateTimeStore.formattedDate, 
                                                        hora_creacion: dateTimeStore.formattedTime }}
    try {
        const responseCab = await fetch(dUrl.urlGlobal + '/api3/insertTpy/', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(dataCabecera)})
         
        if (!responseCab.ok) { error('Error al insertar cabecera'); return }

        // Insertamos los detalles
        for (const fila of detallesActivos) {
            const dataDetalle = { model: "segdept", data: { compania: '010',
                                                            gerencia: filaE.gerencia, 
                                                            departamento: fila.departamento,
                                                            descripcion: fila.descripcion,
                                                            creado_por: userStore.globalUser, 
                                                            fecha_creacion: dateTimeStore.formattedDate, 
                                                            hora_creacion: dateTimeStore.formattedTime,
                                                            status: fila.status, }}
            await fetch(dUrl.urlGlobal + '/api3/insertTpy/', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(dataDetalle)})
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
const upsertDetalle = async (fila: { departamento: string; descripcion: any; tipo_aplica: string; clase: string; subclase: string; status: any }) => {
    if (!fila.departamento) return;
    
    const filaE = registroEnc.value[currentIndexEnc.value]
    try {
        const response = await axios.post(dUrl.urlGlobal + '/api3/querytpy', { tabla: 'segdept', filtro: { compania: '010', gerencia: filaE.gerencia, departamento: fila.departamento} });
        const existe = response.data.length > 0;

        if (!existe) {
            const dataInsert = { model: 'segdept', data: { compania: '010',
                                                           gerencia: filaE.gerencia, 
                                                           departamento: fila.departamento,
                                                           descripcion: fila.descripcion, 
                                                           creado_por: userStore.globalUser, 
                                                           fecha_creacion: dateTimeStore.formattedDate, 
                                                           hora_creacion: dateTimeStore.formattedTime,
                                                           status: fila.status } };
            try { 
                const resInsert = await fetch(dUrl.urlGlobal + '/api3/insertTpy/', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(dataInsert) });
                if (!resInsert.ok) error(`Error insertando la transacción ${fila.departamento}`);
            }
            catch (err: any) {
                error(err.response?.data?.detail || 'Error al actualizar');
            } finally {
                isProcessing.value = false
            }
        } else {
            const dataUpdate = {
                table: 'segdept',
                filters: {
                    compania: '010',
                    gerencia: filaE.gerencia,
                    departamento: fila.departamento,
                },
                data: {
                    descripcion: fila.descripcion,
                    status: fila.status,
                    modificado_por: userStore.globalUser,
                    fecha_status: dateTimeStore.formattedDate,
                    hora_status: dateTimeStore.formattedTime
                }
            };

            Object.keys(dataUpdate.data).forEach(k => {
                if (dataUpdate.data[k as keyof typeof dataUpdate.data] === undefined) delete dataUpdate.data[k as keyof typeof dataUpdate.data];
            });

            const resUpdate = await axios.post(dUrl.urlGlobal + '/api3/updatetpy/', dataUpdate);
            if (resUpdate.status !== 200) error(`Error actualizando la transacción ${fila.departamento}`);
        }
    } catch (err: any) {
        error(err.response?.data?.detail || `Error procesando la transacción ${fila.departamento}`);
    }
};

// Función para manejar la actualización de la cabecera y los detalles
const handleUpdate = async () => {
    if (isProcessing.value) return;
    isProcessing.value = true;

    const filaE = registroEnc.value[currentIndexEnc.value]

     const validados = registros.value.map(r => !r.departamento || !r.descripcion ||
                                                !r.tipo_aplica  || !r.clase || !r.subclase ||
                                                !r.status)

    if (!validados) {
        error('Hay información de departamentos incompleta...')
        return
    }
                                                   
    if (!filaE.gerencia || !filaE.descripcion || !filaE.status) {
        error('Complete la información de Gerencia...')
        return
    }

    const result = await question('Se va a actualizar el registro.', '¿Deseas actualizarlo?');
    if (!result.isConfirmed) return;

    try {
        const responseCab = await axios.post(dUrl.urlGlobal + '/api3/updatetpy/', {
            table: 'seggere',
            filters: { compania: '010', gerencia: filaE.gerencia },
            data: {
                compania: '010',
                gerencia: filaE.gerencia,
                descripcion: filaE.descripcion,
                status: filaE.status,
                modificado_por: userStore.globalUser,
                fecha_status: dateTimeStore.formattedDate,
                hora_status: dateTimeStore.formattedTime
            }
        });

        if (responseCab.status !== 200) {
            error('Error actualizando el Sistema');
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

    const filaE = registroEnc.value[currentIndexEnc.value]
    if (registros.value.length > 0) {
        if (!registros.value[lineaArray]) {
            error('Marque la línea a eliminar...')
            return
        }
        
        let fila_del = registros.value[lineaArray]
        
        const pregunta = await axios.post(dUrl.urlGlobal + '/api3/query', { tabla: 'segdept',
                            filtro: { compania: '010', gerencia: filaE.gerencia,
                                      departamento: fila_del.departamento }})

        if (pregunta.data.lenght > 0) {
            error('Este departamento está definido en afectaciones contables... no puede eliminarse')
            return
        }

        const result = await question(`Se va a eliminar el departamento ${fila_del.departamento}`, '¿Deseas eliminarla?');
        if (!result.isConfirmed) return;

        try {
            //let dataEliminar = { tabla: "scgsgcta", filtro: { tipo_cuenta: formData.value.tipo_cuenta,
            //                                          grupo_cuenta: fila_del.grupo_cuenta }}

            //const pregunta = await fetch(dUrl.urlGlobal + '/api3/insert/', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(dataEliminar)})
            
            const delfila = await axios.post(dUrl.urlGlobal + '/api3/deletetpy', { table: 'segdept', filters: {gerencia: filaE.gerencia, 
                                                                                                            departamento: fila_del.departamento } })
            if (delfila.status !== 200) {
                error(`No se pudo eliminar la transacción ${fila_del.departamento}`)
                return
            }
        }
        catch (err: any) {
            error(err.response?.data?.detail || 'Error inesperado');
        } 
        finally {
            isProcessing.value = false
        }
    }

    const resultado = await question(`Se va a eliminar el sistema ${filaE.gerencia}`, '¿Deseas eliminarlo?');
    if (!resultado.isConfirmed) return;

    try {
        const response = await axios.post(dUrl.urlGlobal + '/api3/delete/', {
            table: 'seggere',
            filters: { sistema: filaE.gerencia } });

        if (response.status !== 200) {
            error('Error al eliminar el registro');
            return;
        }

        success(`Se eliminó el Sistema ${filaE.gerencia}`, 'Evento exitoso')

        // Inactivar los detalles de los registros
        //for (const fila of registros.value) {
        //    if (!fila.grupo_cuenta) continue;
        //    try {
        //        await axios.post(dUrl.urlGlobal + '/api3/update/', {
        //            table: 'scgsgcta',
        //            filters: { tipo_cuenta: formData.value.tipo_cuenta, grupo_cuenta: fila.grupo_cuenta },
        //            data: { status: 'I' }});
        //    } catch (err: any) {
        //        console.log(err);
        //    }
        //}

        //success('Registro y detalles inactivados correctamente', 'Acción exitosa');
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

    const filaE = registroEnc.value[currentIndexEnc.value]
    try {
        // Realizamos la búsqueda a la API
        const response = await axios.post(dUrl.urlGlobal + '/api3/query', 
                        { tabla: 'seggere', filtro: { gerencia: filaE.gerencia,
                                                        descripcion: filaE.descripcion,
                                                        status: filaE.status} });
        // Guardamos los datos obtenidos en dataList
    
        dataList.value = response.data;

        // Establecemos el índice actual en 0
        currentIndex.value = 0;

        // Si hay datos, actualizamos el formulario y detalles
        if (dataList.value.length > 0) {
            updateFormData(); // Actualiza el formulario y detalles con el primer registro
            canNavigate.value = true;
            getSeggere()
            //mode.value = 'view'
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
    //registroEnc.value = [];
    canNavigate.value = false;
};

// ================= AGREGAR / ELIMINAR FILAS =================
function addRowEnc() {
    registroEnc.value.push({
        compania: '',
        gerencia: '',
        descripcion: '',
        status: 'A',
        nom_status: 'Activo'
    });
}

function addRow() {
    registros.value.push({
        departamento: '',
        descripcion: '',
        tipo_aplica: '',
        clase: '',
        subclase: '',
        status: 'A',
        nom_status: 'Activo'
    });
}

function removeRowEnc(indexE: number) {
    registroEnc.value.splice(indexE, 1)
}

function removeRow(index: number) {
    registros.value.splice(index, 1);
    
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
        seggere.value = (await axios.get(`${dUrl.urlGlobal}/api/seggere`)).data;
        segdept.value = (await axios.get(`${dUrl.urlGlobal}/api/segdept`)).data;
        scgclas.value = (await axios.get(`${dUrl.urlGlobal}/api3/scgclas`)).data;
        scgscla.value = (await axios.get(`${dUrl.urlGlobal}/api3/scgscla`)).data;
        scgtapl.value = (await axios.get(`${dUrl.urlGlobal}/api3/scgtapl`)).data

        registroEnc.value = seggere.value.map((i: any) => ({
            compania: i.compania || '',
            gerencia: i.gerencia || '',
            descripcion: i.descripcion || '',
            status: i.status || '',
            nom_status: i.nom_status || ''
        }));

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
