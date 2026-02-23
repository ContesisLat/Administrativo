<template>
  <!-- Botón abrir sidebar -->
  <button class="menu-btn" @click="toggleSidebar">
    ☰
  </button>

  <!-- Overlay oscuro -->
  <div v-if="isSidebarOpen" class="overlay" @click="toggleSidebar"></div>

  <!-- SIDEBAR -->
  <transition name="sidebar">
    <aside v-if="isSidebarOpen" class="sidebar">
      <div class="sidebar-header">
        <h5 class="sidebar-title">Contabilidad General</h5>
        <button class="close-btn" @click="toggleSidebar">✕</button>
      </div>

      <div class="sidebar-body">

        <!-- APLICACIONES -->
        <div v-for="(app, aIndex) in programas" :key="aIndex">

          <!-- Aplicación -->
          <div
            class="app-item"
            :class="{ activeApp: activeApp === aIndex }"
            @click="toggleApp(aIndex)"
          >
            <span>{{ app.aplicacion }}</span>
            <span class="arrow" :class="{ rotate: activeApp === aIndex }">⌄</span>
          </div>

          <!-- PROCESOS -->
          <transition name="app-slide">
            <div v-if="activeApp === aIndex" class="process-container">

              <div
                v-for="(proc, pIndex) in app.procesos"
                :key="pIndex"
                class="process-wrapper"
              >
                <!-- Proceso -->
                <div
                  class="process-item"
                  :class="{ activeProcess: activeProcess === aIndex + '-' + pIndex }"
                  @click="toggleProcess(aIndex, pIndex)"
                >
                  {{ proc.proceso }}
                  <span
                    class="dot"
                    v-if="activeProcess === aIndex + '-' + pIndex"
                  ></span>
                </div>

                <!-- SUBPROGRAMAS FLOTANTES -->
                <transition name="float-right">
                  <div
                    v-if="activeProcess === aIndex + '-' + pIndex"
                    class="sub-floating"
                  >
                    <div
                      v-for="(sub, sIndex) in proc.subprogramas"
                      :key="sIndex"
                      class="sub-item"
                      :class="{ activeSub: activeSub === sub.programa }"
                      @click="openProgram(sub.programa)"
                    >
                      {{ sub.descripcion }}
                    </div>
                  </div>
                </transition>

              </div>

            </div>
          </transition>

        </div>

      </div>
    </aside>
  </transition>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { usePopupStore } from '@/store/PopupStore'
import { UrlGlobal } from '@/store/dominioGlobal'
import { userGlobalStore } from '@/store/userGlobal'

const store = usePopupStore()
const dUrl = UrlGlobal()
const userStore = userGlobalStore()

const usuario = ref<any[]>([])
const perfil = ref('')

// Sidebar estado
const isSidebarOpen = ref(false)
const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value
  if (isSidebarOpen.value) cargarProgramas(perfil.value)
}

onMounted(async () => {
  const responseO = await axios.get(
    dUrl.urlGlobal + `/api/seguser/filter?nombre_usuario=${userStore.globalUser}`
  )
  usuario.value = responseO.data
  perfil.value = usuario.value[0]?.perfil
})

const programas = ref<any[]>([])

const cargarProgramas = async (perfil: string) => {
  try {
    const response = await axios.post(
      dUrl.urlGlobal + '/api/procesos_subprogramas',
      { perfil }
    )
    programas.value = response.data
  } catch (error) {
    console.error('Error cargando programas:', error)
  }
}

/* Estado UI */
const activeApp = ref<number | null>(null)
const activeProcess = ref<string | null>(null)
const activeSub = ref<string | null>(null)

const toggleApp = (index: number) => {
  activeApp.value = activeApp.value === index ? null : index
  activeProcess.value = null
}

const toggleProcess = (aIndex: number, pIndex: number) => {
  const key = aIndex + '-' + pIndex
  activeProcess.value = activeProcess.value === key ? null : key
}

const openProgram = (programa: string) => {
  activeSub.value = programa
  store.openPopup(programa)
}
</script>

<style scoped>
/* ============================= */
/* BOTÓN MENÚ */
/* ============================= */
.menu-btn {
  background: #2563eb;
  color: #fff;
  border: none;
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 15px;
  cursor: pointer;
  transition: all 0.25s ease;
  box-shadow: 0 3px 8px rgba(37, 99, 235, 0.25);
}
.menu-btn:hover {
  background: #1d4ed8;
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(37, 99, 235, 0.35);
}

/* ============================= */
/* OVERLAY OSCURO */
/* ============================= */
.overlay {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.35);
  backdrop-filter: blur(3px);
  z-index: 999;
  transition: opacity 0.3s ease;
}

/* ============================= */
/* SIDEBAR ERP PROFESIONAL */
/* ============================= */
.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 280px;
  background: #ffffff;
  box-shadow: 10px 0 40px rgba(0, 0, 0, 0.08);
  z-index: 1000;
  display: flex;
  flex-direction: column;
}
.sidebar-header {
  padding: 18px;
  border-bottom: 1px solid #eef2f7;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: 600;
}
.sidebar-body {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
}

/* ============================= */
/* TRANSICIONES SIDEBAR */
/* ============================= */
.sidebar-enter-active {
  transition: all 0.35s cubic-bezier(.16,1,.3,1);
}
.sidebar-leave-active {
  transition: all 0.25s ease;
}
.sidebar-enter-from {
  transform: translateX(-100%);
  opacity: 0;
}
.sidebar-enter-to {
  transform: translateX(0);
  opacity: 1;
}
.sidebar-leave-from {
  transform: translateX(0);
  opacity: 1;
}
.sidebar-leave-to {
  transform: translateX(-100%);
  opacity: 0;
}

/* ============================= */
/* BOTÓN CERRAR */
/* ============================= */
.close-btn {
  background: none;
  border: none;
  font-size: 18px;
  cursor: pointer;
  opacity: 0.6;
  transition: 0.2s;
}
.close-btn:hover {
  opacity: 1;
}

/* ============================= */
/* APLICACIONES, PROCESOS Y SUBPROGRAMAS */
/* ============================= */
.app-item {
  padding: 11px 16px;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all 0.25s ease;
  margin-bottom: 5px;
  position: relative;
}
.app-item:hover { background: #f3f4f6; }
.activeApp { background: #eff6ff; color: #2563eb; }
.activeApp::before {
  content: "";
  position: absolute;
  left: -18px;
  top: 20%;
  height: 60%;
  width: 4px;
  border-radius: 4px;
  background: #2563eb;
}
.arrow { transition: transform 0.3s ease; font-size: 12px; opacity: 0.6; }
.rotate { transform: rotate(180deg); }

.process-container { margin-left: 12px; padding-left: 12px; border-left: 1px solid #e5e7eb; }
.process-wrapper { margin-bottom: 4px; }
.process-item {
  padding: 8px 12px;
  font-size: 13px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.25s ease;
  position: relative;
}
.process-item:hover { background: #f9fafb; }
.activeProcess { background: #e0edff; color: #2563eb; }
.dot {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  width: 6px;
  height: 6px;
  background: #2563eb;
  border-radius: 50%;
}

.sub-floating { margin-top: 4px; margin-left: 14px; padding-left: 10px; border-left: 1px dashed #e5e7eb; }
.sub-item {
  padding: 6px 10px;
  font-size: 12.5px;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.25s ease;
  color: #4b5563;
}
.sub-item:hover { background: #f3f4f6; }
.activeSub { background: #eff6ff; color: #2563eb; font-weight: 500; }

/* ============================= */
/* TRANSICIONES INTERIORES VUE */
/* ============================= */
.app-slide-enter-active, .app-slide-leave-active { transition: all 0.25s ease; }
.app-slide-enter-from, .app-slide-leave-to { opacity: 0; transform: translateY(-6px); }
.float-right-enter-active, .float-right-leave-active { transition: all 0.2s ease; }
.float-right-enter-from, .float-right-leave-to { opacity: 0; transform: translateY(-4px); }

</style>


