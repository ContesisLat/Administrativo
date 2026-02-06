import { defineStore } from 'pinia';

export const usePopupStore = defineStore('popup', {
  state: () => ({
    popupComponentName: "",
    openedPopups: [] as { componentName: string, width: number, height: number, posX: number, posY: number }[],
  }),
  actions: {
    openPopup(componentName: string) {
      let wth = 50
      let hgt = 50

      if (window.innerWidth > 600) {
        wth = 1000
        hgt = 500
      }else if (window.innerWidth < 600){
        wth = 450
        hgt = 420
      }

      this.openedPopups.push({
        componentName: componentName,
        width: wth, // Valor predeterminado para el ancho
        height: hgt, // Valor predeterminado para el alto
        posX: 0, // Valor predeterminado para la posición X
        posY: 0, // Valor predeterminado para la posición Y
      });
      this.popupComponentName = componentName;
    },
    closePopup(index:number) {
      // Implementación del cierre de la ventana emergente
      this.openedPopups.splice(index, 1);
    },
  },
});
