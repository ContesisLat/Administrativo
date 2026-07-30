<template>
    <div class="full-background">
        <DropDown />
        <FloatingTools />
        <PopupWindow />
    </div>
</template>

<script lang="ts" setup>
import DropDown from '@/views/EstructuraS/DropDown.vue'
import FloatingTools from '@/views/EstructuraS/FloatingTools.vue';
import PopupWindow from '@/views/EstructuraS/PopupWindow.vue';
</script>

<style scoped>
.full-background {
  min-height: 100vh;
  position: relative;
  z-index: 1000;
  overflow: hidden;

  
  background: linear-gradient(
    180deg,
    #bcd6e6 0%,   
    #dcecf5 50%, 
    #f4f9fc 100% 
  );
   
}


.full-background::before {
  content: "";
  position: absolute;
  inset: -200px;

  background:
    radial-gradient(circle at 30% 30%, rgba(255,255,255,0.75), transparent 60%),
    radial-gradient(circle at 70% 25%, rgba(255,255,255,0.65), transparent 65%),
    radial-gradient(circle at 50% 60%, rgba(255,255,255,0.55), transparent 70%),
    radial-gradient(circle at 80% 70%, rgba(255,255,255,0.5), transparent 75%);

  filter: blur(100px);
  z-index: -1;
}


.full-background::after {
  content: "";
  position: absolute;
  inset: -150px;

  background:
    radial-gradient(circle at 20% 80%, rgba(200,220,235,0.4), transparent 70%),
    radial-gradient(circle at 85% 60%, rgba(210,230,245,0.35), transparent 70%);

  filter: blur(120px);
  z-index: -1;
}

html {
  scroll-behavior: smooth;
}
</style>