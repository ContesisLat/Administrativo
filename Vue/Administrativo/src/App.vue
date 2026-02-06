<template>
  <router-view/>
</template>

<script lang="ts" setup>
import PageLogin from './components/PageLogin.vue';
</script>

<style>
#app {
  position: absolute;
  width: 100%;
  height: 100%;
  background: white;
  background-image: url('@/assets/ContesisLA.png');
  background-repeat: no-repeat;
  background-size:84%;
  background-position: 50% 25%;
}
</style>
