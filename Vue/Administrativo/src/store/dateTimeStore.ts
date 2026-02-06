// stores/dateTimeStore.ts
import { defineStore } from 'pinia';

export const useDateTimeStore = defineStore('dateTime', {
  state: () => ({
    currentDate: new Date() as Date,
  }),
  actions: {
    refreshDateTime() {
      this.currentDate = new Date();
    },
  },
  getters: {
    formattedDate: (state) => {
      const date = state.currentDate;
      const day = date.getDate().toString().padStart(2, '0');
      const month = (date.getMonth() + 1).toString().padStart(2, '0'); // Los meses van de 0 a 11
      const year = date.getFullYear();
      return `${year}-${month}-${day}`;
    },
    formattedTime: (state) => {
      const date = state.currentDate;
      const hours = date.getHours().toString().padStart(2, '0');
      const minutes = date.getMinutes().toString().padStart(2, '0');
      const seconds = date.getSeconds().toString().padStart(2, '0');
      //const time_p = date.getMilliseconds().toString().padStart(6, '0')
      return `${hours}:${minutes}:${seconds}`;
    },
  },
});
