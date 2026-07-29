// stores/globalStore.ts
import { defineStore } from 'pinia';

export const userGlobalStore = defineStore('Uglobal', {
  state: () => ({
    globalUser: '' as string, // Variable global inicializada como string vacía
    Compania: '' as string,
    Agencia: '' as string,
  }),
  actions: {
    // Método para actualizar la variable global
    setUser(newValue: string) {
      this.globalUser = newValue;
    },
    setCompania(newValue: string) {
      this.Compania = newValue;
    },
    setAgencia(newValue: string){
      this.Agencia = newValue
    }
  },
});
