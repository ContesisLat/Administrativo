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
  background-color: white;
  background-image: url('@/assets/ContesisLA.png');
  background-repeat: no-repeat;
  background-size: 90%;
  background-position: 50% 90px;
  position: relative;
  z-index: 1000;
}

html {
  scroll-behavior: smooth;
}
</style>