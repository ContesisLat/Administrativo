<template>
  <div class="popup-window" v-for="(popup, index) in openedPopups" :key="index"
    :style="{ top: popup.posY + 'px', left: popup.posX + 'px', width: popup.width + 'px', height: popup.height + 'px' }"
    @mousedown="startDrag($event, index)">
    <div class="content">
      <!-- Contenido de la ventana emergente -->
      <component :is="getComponentName(index)" />
    </div>
    <div class="btn-group">
      <button @click="store.closePopup(index)"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x"
          viewBox="0 0 16 16">
          <path
            d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708" />
        </svg>
      </button>
      <button @mousedown="startResize($event, index)"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
          class="bi bi-textarea-resize" viewBox="0 0 16 16">
          <path
            d="M0 4.5A2.5 2.5 0 0 1 2.5 2h11A2.5 2.5 0 0 1 16 4.5v7a2.5 2.5 0 0 1-2.5 2.5h-11A2.5 2.5 0 0 1 0 11.5zM2.5 3A1.5 1.5 0 0 0 1 4.5v7A1.5 1.5 0 0 0 2.5 13h11a1.5 1.5 0 0 0 1.5-1.5v-7A1.5 1.5 0 0 0 13.5 3zm10.854 4.646a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708l3-3a.5.5 0 0 1 .708 0m0 2.5a.5.5 0 0 1 0 .708l-.5.5a.5.5 0 0 1-.708-.708l.5-.5a.5.5 0 0 1 .708 0" />
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup>
import { usePopupStore } from "@/store/PopupStore";
import globalComponents from "@/store/global-component";
import { ref, computed, watch } from 'vue';

const store = usePopupStore();
const openedPopups = computed(() => store.openedPopups);

// para indicar si se está redimensionando
let isResizing = false;

const startDrag = (event, index) => {
  if (!event || !event.clientX || !event.clientY || isResizing) return;
  const popup = openedPopups.value[index];
  const startX = event.clientX - popup.posX;
  const startY = event.clientY - popup.posY;

  const handleDrag = (event) => {
    if (!event.clientX || !event.clientY) return;
    popup.posX = event.clientX - startX;
    popup.posY = event.clientY - startY;
  };

  const stopDrag = () => {
    document.removeEventListener('mousemove', handleDrag);
    document.removeEventListener('mouseup', stopDrag);
  };

  document.addEventListener('mousemove', handleDrag);
  document.addEventListener('mouseup', stopDrag);
};

const startResize = (event, index) => {
  if (!event || !event.clientX || !event.clientY) return;
  const popup = openedPopups.value[index];
  let startX = event.clientX;
  let startY = event.clientY;

  // Cambiar a true durante la operación de redimensionamiento
  isResizing = true;

  const handleResize = (event) => {
    if (!event.clientX || !event.clientY) return;
    popup.width = Math.max(100, popup.width + event.clientX - startX);
    popup.height = Math.max(100, popup.height + event.clientY - startY);
    startX = event.clientX;
    startY = event.clientY;
  };

  const stopResize = () => {
    document.removeEventListener('mousemove', handleResize);
    document.removeEventListener('mouseup', stopResize);
    // Restaurar a false al finalizar la operación de redimensionamiento
    isResizing = false;
  };

  document.addEventListener('mousemove', handleResize);
  document.addEventListener('mouseup', stopResize);
};

const getComponentName = (index) => {
  const componentName = openedPopups.value[index].componentName;
  return globalComponents[componentName];
};

const centerPopup = (index) => {
  const windowWidth = window.innerWidth;
  const windowHeight = window.innerHeight;

  const popup = openedPopups.value[index];
  if (popup) {
    popup.posX = (windowWidth - popup.width) / 2;
    popup.posY = (windowHeight - popup.height) / 2;
  }
};

let previousLength = 0;

watch(() => openedPopups.value.length, (newValue) => {
  if (newValue > previousLength) {
    const lastIndex = newValue - 1; // Índice del último popup agregado
    centerPopup(lastIndex);
  }
  previousLength = newValue; // Actualizar el valor anterior
});

</script>

<style scoped>
.popup-window {
  position: absolute;
  background-color: transparent;
  border: 2px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  overflow: hidden;
}

.content {
  position: relative;
  width: 100%;
  height: 100%;
}


.btn-group {
  display: flex;
  justify-content: flex-end;
  position: absolute;
  bottom: 7px;
  right: 10px;
  gap: 5px;
  background-color: #24292F;
  border: none;
  border-radius: 3px;
}

.btn-group button {
  background-color: transparent;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.btn-group button:hover {
  background-color: #4c4d54;
}
</style>
