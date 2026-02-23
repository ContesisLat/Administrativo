<template>
  <div class="popup-window" v-for="(popup, index) in openedPopups" :key="index" :style="{
    top: popup.posY + 'px',
    left: popup.posX + 'px',
    width: popup.width + 'px',
    height: popup.height + 'px'
  }">
    <!-- HEADER MODERNO -->
    <div class="popup-header" @mousedown="startDrag($event, index)">
      <div class="popup-title">
        {{ popup.componentName }}
      </div>

      <div class="window-controls">
        <button class="control-btn close" @click="store.closePopup(index)">
          ✕
        </button>
      </div>
    </div>

    <!-- CONTENIDO -->
    <div class="popup-content">
      <component :is="getComponentName(index)" />
    </div>

    <!-- RESIZE HANDLE -->
    <div class="resize-handle" @mousedown="startResize($event, index)"></div>
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
/* =========================
   POPUP CONTAINER
========================= */

.popup-window {
  position: absolute;
  display: flex;
  flex-direction: column;

  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);

  background: rgba(255, 255, 255, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.85);

  border-radius: 22px;

  box-shadow:
    0 30px 80px rgba(0, 0, 0, 0.12),
    0 10px 30px rgba(0, 0, 0, 0.06);

  overflow: hidden;

  animation: popupFade 0.28s cubic-bezier(.22,.61,.36,1);
  transition: box-shadow 0.3s ease;
}

.popup-window:hover {
  box-shadow:
    0 35px 90px rgba(0, 0, 0, 0.14),
    0 12px 35px rgba(0, 0, 0, 0.07);
}

/* =========================
   ANIMATION
========================= */

@keyframes popupFade {
  from {
    opacity: 0;
    transform: scale(0.96) translateY(8px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

/* =========================
   HEADER
========================= */

.popup-header {
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;

  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);

  border-bottom: 1px solid rgba(255, 255, 255, 0.8);

  cursor: grab;
  user-select: none;

  transition: background 0.25s ease;
}

.popup-header:active {
  cursor: grabbing;
}

.popup-title {
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.6px;
  color: #444;
  text-transform: uppercase;
}

/* =========================
   CONTENT AREA
========================= */

.popup-content {
  flex: 1;
  overflow: auto;
  padding: 22px;
  color: #2c2c2c;
}

/* =========================
   WINDOW CONTROLS
========================= */

.window-controls {
  display: flex;
  gap: 8px;
}

.control-btn {
  width: 30px;
  height: 30px;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.25s ease;

  backdrop-filter: blur(10px);
}

/* Close Button */
.control-btn.close {
  background: rgba(255, 95, 87, 0.15);
  color: #d64545;
}

.control-btn.close:hover {
  background: #e54848;
  color: white;
  transform: scale(1.08);
  box-shadow: 0 8px 20px rgba(229, 72, 72, 0.3);
}

/* =========================
   RESIZE HANDLE
========================= */

.resize-handle {
  width: 16px;
  height: 16px;
  position: absolute;
  right: 10px;
  bottom: 10px;
  cursor: se-resize;
  border-radius: 6px;

  background: linear-gradient(
    135deg,
    transparent 40%,
    rgba(0, 0, 0, 0.25) 40%,
    rgba(0, 0, 0, 0.25) 60%,
    transparent 60%
  );

  opacity: 0.35;
  transition: 0.25s ease;
}

.resize-handle:hover {
  opacity: 0.75;
}

</style>
