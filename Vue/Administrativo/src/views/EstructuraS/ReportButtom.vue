<template>
    <div class="modal-backdrop" v-if="props.CardReport==true" @click="handleClick"></div>
    <div class="ReportPage" v-if="props.CardReport==true">
        <h4>Correo a @ContesisLa</h4>
        <hr>
        <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label">Correo Electronico</label>
            <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com" v-model="email" style="background-color: transparent; color: black;">
        </div>
        <div class="mb-3">
            <label for="exampleFormControlTextarea1" class="form-label">Mensaje</label>
            <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" v-model="mensaje" style="resize: vertical; background-color: transparent; color: black;"></textarea>
        </div>
        <div class="mb-3">
            <label for="formFile" class="form-label">Agregar Archivo</label>
            <input class="form-control" type="file" id="formFile" @change="handleFileUpload" style="background-color: transparent; color: black;">
        </div>
        <hr>
        <div class="SuccessButoms"><button @click="handleClick">cancelar</button><button @click="enviarCorreo" style="background-color:#001982">enviar</button></div>

    </div>
</template>

<script lang="ts" setup>
import { defineProps,defineEmits,Ref,ref } from 'vue'
import { UrlGlobal } from '@/store/dominioGlobal';

const dUrl = UrlGlobal()

const props = defineProps({
    CardReport: Boolean,
})
const emits = defineEmits(['updateProps'])
        const handleClick = () =>{
            emits("updateProps",!props.CardReport)
        }


//envio de correo----------------------------------------------------
const email = ref('');
const mensaje = ref('');
const archivo = ref<File | null>(null);

// Función para capturar el archivo subido
const handleFileUpload = (event: Event) => {
  const target = event.target as HTMLInputElement;
  archivo.value = target.files ? target.files[0] : null;
};

// Función para enviar el correo
const enviarCorreo = async () => {
  const formData = new FormData();
  formData.append('correo_remitente', email.value);
  formData.append('mensaje', mensaje.value);
  
  if (archivo.value) {
    formData.append('archivo', archivo.value);
  }

  try {
    const response = await fetch(dUrl.urlGlobal +'/api/envio_correo', {
      method: 'POST',
      body: formData,
    });

    const data = await response.json();

    if (data.status === 'success') {
      alert('Correo enviado correctamente');
      email.value = '';
      mensaje.value = '';
      archivo.value = null;
    } else {
      alert(`Error: ${data.message}`);
    }
  } catch (error) {
    alert('Ocurrió un error al enviar el correo');
    console.error(error);
  }
};
//-------------------------------------------------------------------
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

svg{
    fill: black;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Fondo oscuro semitransparente */
  z-index: 1050; /* Coloca el fondo oscuro por encima de otros elementos */
  
}
.ReportPage{
    min-height: 250px;
    width: 550px;
    background: whitesmoke;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 8px;
    display: flex;
    justify-content:left;
    align-items: left;
    display: flex;
    flex-direction: column;
    gap: 15px;
    font-family: 'Poppins', sans-serif;
    color: black;
    padding: 15px;
    z-index: 1060;
    @media screen and (max-width: 600px) {
    width: 340px;
  }
}
.ReportPage hr{
    border: none;
    border-top: 1px solid #ccc;
    margin:1px 0;
    padding-left: 100%;
}

.SuccessButoms{
    justify-content:right;
    align-items:right;
    flex-direction: row;
    display: flex;
    gap: 10px;
    margin-bottom: 5px;
}
.SuccessButoms button{
    border: none;
    border-radius: 4px;
    background-color: #24292F;
    color: white;
    font-family: 'Poppins', sans-serif;
    width: 90px;
    font-size: small;
    padding: 3px;
}
</style>