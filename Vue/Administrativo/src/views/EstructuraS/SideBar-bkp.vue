<template>
  <!-- Botón para abrir el menú -->
  <a class="btn" @click="cargarProgramas(perfil)" data-bs-toggle="offcanvas" href="#offcanvasExample" role="button"
    aria-controls="offcanvasExample" style="color: white;">
    ☰
  </a>

  <!-- Panel lateral -->
  <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel"
    style="font-family: Trebuchet MS;">
    <div class="offcanvas-header">
      <h5 class="offcanvas-title" id="offcanvasExampleLabel">Imagen</h5>
      <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
    </div>

    <div class="offcanvas-body d-flex flex-column gap-2">
      <!-- Iteramos sobre los programas -->
      <div class="btn-group dropend" v-for="(programa, index) in programas" :key="index">
        <!-- Nombre del programa -->
        <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" href="#" aria-expanded="false">
          {{ programa.proceso }}
        </a>

        <!-- Subprogramas -->
        <ul class="dropdown-menu" style="cursor: pointer;">
          <li v-for="(sub, i) in programa.subprogramas" :key="i" @click="store.openPopup(sub.programa)">
            <a class="dropdown-item">{{ sub.programa }}</a>
          </li>

          <!-- Si no tiene subprogramas -->
          <li v-if="programa.subprogramas.length === 0">
            <a class="dropdown-item disabled" aria-disabled="true">
              Sin subprogramas
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>


<script lang="ts" setup>
import { usePopupStore } from '@/store/PopupStore';
import { ref, watch, computed, onMounted } from 'vue'
import axios from 'axios';
import { UrlGlobal } from '@/store/dominioGlobal';
import { userGlobalStore } from '@/store/userGlobal';

const store = usePopupStore()
const dUrl = UrlGlobal()
const userStore = userGlobalStore()

const usuario = ref<any[]>([]);
const perfil = ref('')
onMounted(async () => {
  const responseO = await axios.get(dUrl.urlGlobal + `/api/seguser/filter?nombre_usuario=${userStore.globalUser}`)
  usuario.value = responseO.data
  perfil.value = usuario.value[0]?.perfil
})

const programas = ref<any[]>([]);
const cargarProgramas = async (perfil: string) => {
  try {
    const response = await axios.post(dUrl.urlGlobal + "/api/procesos_subprogramas", {
      perfil: perfil,
    });
    programas.value = response.data;
    console.log(programas.value)
  } catch (error) {
    console.error("Error cargando programas:", error);
  }
};


</script>

<style scoped></style>
