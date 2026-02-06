<template>
    <div class="modal-backdrop" v-if="props.device == true" @click="handleClick"></div>
    <div class="DevicePage" v-if="props.device == true">
        <div class="devices">
            <div>
                <video v-if="isCameraActive" ref="video" width="350" height="200" autoplay></video>
                <img v-if="photo" :src="photo" alt="Foto tomada" />
                <canvas ref="canvas" width="330" height="200" style="display: none;"></canvas>
            </div>
        </div>
        <div class="conteiner">
            <h5>Manifiestos</h5>
            <hr>
            <div class="card overflow-scroll d-flex">
                <table class="table table-hover table-sm">
                    <thead>
                        <tr>
                            <th>info</th>
                            <th>info</th>
                            <th>info</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td></td>
                            <td></td>
                            <td></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <hr>
        <!-- Solo mostramos el video cuando la cámara está activa -->
        <div class="SuccessButoms">
            <button @click="changeCamera" v-if="cameras.length">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-arrow-repeat" viewBox="0 0 16 16">
                    <path
                        d="M11.534 7h3.932a.25.25 0 0 1 .192.41l-1.966 2.36a.25.25 0 0 1-.384 0l-1.966-2.36a.25.25 0 0 1 .192-.41m-11 2h3.932a.25.25 0 0 0 .192-.41L2.692 6.23a.25.25 0 0 0-.384 0L.342 8.59A.25.25 0 0 0 .534 9" />
                    <path fill-rule="evenodd"
                        d="M8 3c-1.552 0-2.94.707-3.857 1.818a.5.5 0 1 1-.771-.636A6.002 6.002 0 0 1 13.917 7H12.9A5 5 0 0 0 8 3M3.1 9a5.002 5.002 0 0 0 8.757 2.182.5.5 0 1 1 .771.636A6.002 6.002 0 0 1 2.083 9z" />
                </svg>
            </button>
            <button v-if="!isCameraActive" @click="startCamera"><svg xmlns="http://www.w3.org/2000/svg" width="16"
                    height="16" fill="currentColor" class="bi bi-upc-scan" viewBox="0 0 16 16">
                    <path
                        d="M1.5 1a.5.5 0 0 0-.5.5v3a.5.5 0 0 1-1 0v-3A1.5 1.5 0 0 1 1.5 0h3a.5.5 0 0 1 0 1zM11 .5a.5.5 0 0 1 .5-.5h3A1.5 1.5 0 0 1 16 1.5v3a.5.5 0 0 1-1 0v-3a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 1-.5-.5M.5 11a.5.5 0 0 1 .5.5v3a.5.5 0 0 0 .5.5h3a.5.5 0 0 1 0 1h-3A1.5 1.5 0 0 1 0 14.5v-3a.5.5 0 0 1 .5-.5m15 0a.5.5 0 0 1 .5.5v3a1.5 1.5 0 0 1-1.5 1.5h-3a.5.5 0 0 1 0-1h3a.5.5 0 0 0 .5-.5v-3a.5.5 0 0 1 .5-.5M3 4.5a.5.5 0 0 1 1 0v7a.5.5 0 0 1-1 0zm2 0a.5.5 0 0 1 1 0v7a.5.5 0 0 1-1 0zm2 0a.5.5 0 0 1 1 0v7a.5.5 0 0 1-1 0zm2 0a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5zm3 0a.5.5 0 0 1 1 0v7a.5.5 0 0 1-1 0z" />
                </svg>
            </button>
            <button v-if="isCameraActive" @click="takePicture"><svg xmlns="http://www.w3.org/2000/svg" width="16"
                    height="16" fill="currentColor" class="bi bi-camera" viewBox="0 0 16 16">
                    <path
                        d="M15 12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h1.172a3 3 0 0 0 2.12-.879l.83-.828A1 1 0 0 1 6.827 3h2.344a1 1 0 0 1 .707.293l.828.828A3 3 0 0 0 12.828 5H14a1 1 0 0 1 1 1zM2 4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-1.172a2 2 0 0 1-1.414-.586l-.828-.828A2 2 0 0 0 9.172 2H6.828a2 2 0 0 0-1.414.586l-.828.828A2 2 0 0 1 3.172 4z" />
                    <path
                        d="M8 11a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5m0 1a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7M3 6.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0" />
                </svg>
            </button>
            <button v-if="!isCameraActive" @click="sendImage"><svg xmlns="http://www.w3.org/2000/svg" width="16"
                    height="16" fill="currentColor" class="bi bi-send" viewBox="0 0 16 16">
                    <path
                        d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z" />
                </svg></button>
            <button v-if="!isCameraActive" @click="removePhoto"><svg xmlns="http://www.w3.org/2000/svg" width="16"
                    height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                    <path
                        d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z" />
                    <path
                        d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z" />
                </svg>
            </button>
        </div>



    </div>

</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
//import { defineProps, defineEmits } from 'vue';
import axios from 'axios';
import { UrlGlobal } from '@/store/dominioGlobal';

const dUrl = UrlGlobal()

const video = ref<HTMLVideoElement | null>(null);
const canvas = ref<HTMLCanvasElement | null>(null);
const photo = ref<string | null>(null);
const isCameraActive = ref(false); // Nueva variable para gestionar el estado de la cámara
let stream: MediaStream | null = null; // Variable para almacenar el stream
const cameras = ref<MediaDeviceInfo[]>([]); // Almacenar cámaras disponibles
const currentCameraIndex = ref(0); // Índice de la cámara actual

// Listar las cámaras disponibles
const listCameras = async () => {

    try {
        await navigator.mediaDevices.getUserMedia({ video: true }); // Solicita permiso
        const devices = await navigator.mediaDevices.enumerateDevices()
        cameras.value = devices.filter(device => device.kind === 'videoinput');
        if (cameras.value.length > 0) {
            currentCameraIndex.value = 0; // Seleccionar la primera cámara por defecto
        }
    } catch (error) {
        console.error('Error al obtener las cámaras:', error);
    }
};

onMounted(() =>{

    listCameras();
})

// Iniciar la cámara
const startCamera = async () => {
    photo.value = null;
    isCameraActive.value = true;
    try {
        // Asegúrate de que hay cámaras disponibles
        const devices = await navigator.mediaDevices.enumerateDevices();
        cameras.value = devices.filter(device => device.kind === 'videoinput');

        if (cameras.value.length === 0) {
            console.error('No se encontraron cámaras disponibles.');
            alert('No se encontraron cámaras disponibles.');
            return;
        }

        // Verifica que el índice actual sea válido
        if (currentCameraIndex.value < 0 || currentCameraIndex.value >= cameras.value.length) {
            console.error('Índice de cámara no válido.');
            alert('Índice de cámara no válido.');
            return;
        }

        const cameraId = cameras.value[currentCameraIndex.value].deviceId; // ID de la cámara actual
        
        // Intentar acceder a la cámara
        stream = await navigator.mediaDevices.getUserMedia({
            video: { deviceId: { exact: cameraId } }
        });

        if (video.value) {
            video.value.srcObject = stream;
        }
    } catch (err) {
        console.error('Error accediendo a la cámara:', err);
        isCameraActive.value = false;
        alert('Error accediendo a la cámara: ' + err); // Mostrar mensaje de error
    }
};


// Cambiar entre cámaras
const changeCamera = async () => {
    // Detener el stream actual
    if (stream) {
        const tracks = stream.getTracks();
        tracks.forEach(track => track.stop());
    }

    // Incrementar el índice de la cámara actual
    currentCameraIndex.value = (currentCameraIndex.value + 1) % cameras.value.length;

    // Iniciar la nueva cámara
    await startCamera();
};


// Tomar la foto, guardarla en Vue y detener la cámara
const takePicture = () => {
    if (video.value && canvas.value && stream) {
        const context = canvas.value.getContext('2d');
        if (context) {
            context.drawImage(video.value, 0, 0, canvas.value.width, canvas.value.height);
            // Convertir la imagen en base64 y almacenarla
            photo.value = canvas.value.toDataURL('image/png');
        }

        // Detener la cámara cerrando todas las pistas del stream
        const tracks = stream.getTracks();
        tracks.forEach(track => track.stop());
        stream = null; // Liberar el stream después de detenerlo
        isCameraActive.value = false;
    }
};

// para eliminar la foto-------------------------------
const removePhoto = () => {
    photo.value = null
}
//-----------------------------------------------------

//envio del codigo de barra---------------------------------------------------------------------
async function sendImage() {
    if (photo.value) {
        // Convertimos la imagen en base64 a un Blob
        const base64Response = await fetch(photo.value);
        const blob = await base64Response.blob();
        // Creamos un FormData y añadimos la imagen como archivo
        const formData = new FormData();
        formData.append('barcode_image', blob, 'barcode.png');

        try {
            const response = await axios.post(dUrl.urlGlobal + '/api/barcode', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });

            if (response.status === 200) {
                console.log('Código de barras detectado:', response.data.barcode_data);
                alert(`Código de barras detectado: ${response.data.barcode_data}`);
            } else {
                console.error('Error al procesar la imagen:', response.data.error);
            }
        } catch (error) {
            alert('No se detecta codigo de barras en la imagen')
            console.error('Error en la solicitud:', error);
        }
    }
}
//---------------------------------------------------------------------------------------------


// props y emits----------------------------------------------------------------

const props = defineProps({
    device: Boolean,
})
const emits = defineEmits(['DevicesProps'])
const handleClick = () => {
       // detener cámara si está activa
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
        stream = null;
    }
    isCameraActive.value = false;
    photo.value = null;

    emits("DevicesProps", !props.device)
}
//-------------------------------------------------------------------------------
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

.modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    /* Fondo oscuro semitransparente */
    z-index: 3;
    /* Coloca el fondo oscuro por encima de otros elementos */

}

.DevicePage {
    min-height: 550px;
    width: 450px;
    background: whitesmoke;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    gap: 15px;
    font-family: 'Poppins', sans-serif;
    text-decoration: dashed;
    color: black;
    padding: 15px;
    z-index: 3;

    @media screen and (max-width: 600px) {
        width: 340px;
    }
}

.DevicePage hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 1px 0;
    padding-left: 100%;
}

.SuccessButoms {
    justify-content: right;
    align-items: right;
    flex-direction: row;
    display: flex;
    gap: 10px;
    margin-bottom: 5px;
}

.SuccessButoms button {
    border: none;
    border-radius: 20px;
    padding: 3px;
}

.devices {
    justify-content: center;
    align-items: center;
    display: flex;
    overflow: hidden;
}

.devices div {
    justify-content: center;
    align-items: center;
    display: flex;
    width: 350px;
    height: 250px;
    border-radius: 5px;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset;
    margin: 4px;
}

.conteiner {
    display: flex;
    gap: 5px;
    flex-direction: column;
}

.conteiner h5 {
    padding-left: 8%;
}

.card {
    width: 100%;
    height: 150px;
    min-width: min-content;
    min-height: min-content;
    box-sizing: border-box;
}
</style>