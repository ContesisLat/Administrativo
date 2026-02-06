<template>
    <ReportButtom :CardReport="CardReport" @updateProps="updatePropsValue"/>
    <DeviceC :device="device" @DevicesProps="updatePropsD"/>
    <div class="fab-container">
        <div class="fab shadow">
            <div class="fab-content">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-layers-fill" viewBox="0 0 16 16">
                    <path d="M7.765 1.559a.5.5 0 0 1 .47 0l7.5 4a.5.5 0 0 1 0 .882l-7.5 4a.5.5 0 0 1-.47 0l-7.5-4a.5.5 0 0 1 0-.882l7.5-4z"/>
                    <path d="m2.125 8.567-1.86.992a.5.5 0 0 0 0 .882l7.5 4a.5.5 0 0 0 .47 0l7.5-4a.5.5 0 0 0 0-.882l-1.86-.992-5.17 2.756a1.5 1.5 0 0 1-1.41 0z"/>
            </svg>
            </div>
        </div>
        <div class="sub-button shadow">
            <a href="https://www.office.com/launch/word" target="_blank" title="Word">
            <img src="@/assets/office.png" alt="word" class="logo-image"></a>
        </div>
        <div class="sub-button shadow">
            <a href="#" @click.prevent="ReportOpen"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chat" viewBox="0 0 16 16">
                <path d="M2.678 11.894a1 1 0 0 1 .287.801 10.97 10.97 0 0 1-.398 2c1.395-.323 2.247-.697 2.634-.893a1 1 0 0 1 .71-.074A8.06 8.06 0 0 0 8 14c3.996 0 7-2.807 7-6 0-3.192-3.004-6-7-6S1 4.808 1 8c0 1.468.617 2.83 1.678 3.894m-.493 3.905a21.682 21.682 0 0 1-.713.129c-.2.032-.352-.176-.273-.362a9.68 9.68 0 0 0 .244-.637l.003-.01c.248-.72.45-1.548.524-2.319C.743 11.37 0 9.76 0 8c0-3.866 3.582-7 8-7s8 3.134 8 7-3.582 7-8 7a9.06 9.06 0 0 1-2.347-.306c-.52.263-1.639.742-3.468 1.105z"/>
            </svg></a>
        </div>
        <div class="sub-button shadow">
            <a href="https://www.google.com/intl/es/gmail/about/" target="_blank" title="Gmail">
            <img src="@/assets/Gmail-logo.png" alt="word" class="logo-image"></a>
        </div>
        <div class="sub-button shadow">
            <a href="#" @click.prevent="deviceOpen"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-upc"
                viewBox="0 0 16 16">
                <path
                    d="M3 4.5a.5.5 0 0 1 1 0v7a.5.5 0 0 1-1 0zm2 0a.5.5 0 0 1 1 0v7a.5.5 0 0 1-1 0zm2 0a.5.5 0 0 1 1 0v7a.5.5 0 0 1-1 0zm2 0a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5zm3 0a.5.5 0 0 1 1 0v7a.5.5 0 0 1-1 0z" />
            </svg></a>
        </div>
    </div>
</template>

<script lang="ts" setup>
import ReportButtom from './ReportButtom.vue';
import DeviceC from './DeviceC.vue';
import {ref} from 'vue';

let CardReport = ref(false);
const ReportOpen=()=>{
    CardReport.value = !CardReport.value
}

function updatePropsValue(newValue:boolean){
    CardReport.value = newValue
}

//emits y props de DeviceC------------------------------
let device = ref(false);
const deviceOpen = () =>{
    device.value =!device.value
}

function updatePropsD(newValue:boolean){
    device.value = newValue
}
</script>

<style scoped>
.fab-container{
       display: flex;
     flex-direction: column;
     justify-content: flex-end;
     align-items: center;
     user-select: none;
    position: absolute;
    position: fixed;
     bottom: 30px;
     right: 30px;
     z-index: 2000; /* añade esto para que siempre quede encima */
}
.fab-container svg{
    fill: white;
}
.fab-container:hover{
    height: 100%;
}
.fab-container:hover .sub-button:nth-child(2){
    transform: translateY(-60px);
}
.fab-container .fab .fab-content
.logo-image{
    color: white;
    font-size: 48px;
}
.fab-container .sub-button{
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    bottom: 10px;
    right: 10px;
    height: 30px;
    width: 30px;
    background-color: transparent;
    border-radius: 50%;
    transition: all 0.3s ease;
}
.fab-container .sub-button
.logo-image{
    height: 30px;
    width: 30px;
   
}

.fab-container:hover .sub-button:nth-child(3){
    transform: translateY(-110px);
}
.fab-container:hover .sub-button:nth-child(4){
    transform: translateY(-150px);
}
.fab-container:hover .sub-button:nth-child(5){
    transform: translateY(-200px);
}
.fab-container:hover .sub-button:nth-child(6){
    transform: translateY(-320px);
}
.fab-container .fab{
    position: relative;
    height: 50px;
    width: 50px;
    background-color:#001982;
    border-radius: 50%;
    z-index: 2;
}

.fab-container .fab .fab-content{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    width: 100%;
    border-radius: 50%;
}
.sub-button svg{
    fill: black;
}
</style>