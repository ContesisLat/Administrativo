// stores/globalStore.ts
import { defineStore } from 'pinia';

export const userGlobalStore = defineStore('Uglobal', {
  state: () => ({
    globalUser: '' as string, // Variable global inicializada como string vacía
  }),
  actions: {
    // Método para actualizar la variable global
    setUser(newValue: string) {
      this.globalUser = newValue;
    },
  },
});
