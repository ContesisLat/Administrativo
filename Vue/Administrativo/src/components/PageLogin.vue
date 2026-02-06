<template>
  <div id="app2">
    <div class="form">
      <h4 style="font-family:Lucida Handwriting,cursive"><b>Login</b></h4>
      <h2>Contesis <br>Latinoamerica</h2><br>

      <div class="inputbox">
        <input v-model="username" type="text" required id="User" autocomplete="off">
        <label for="User">Usuario</label>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person"
          viewBox="0 0 16 16">
          <path
            d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6m2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0m4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4m-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664z" />
        </svg>
      </div>

      <div class="inputbox">
        <input v-model="password" type="password" required id="password">
        <label for="password">Contraseña</label>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-lock"
          viewBox="0 0 16 16">
          <path
            d="M8 1a2 2 0 0 1 2 2v4H6V3a2 2 0 0 1 2-2zm3 6V3a3 3 0 0 0-6 0v4a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2zM5 8h6a1 1 0 0 1 1 1v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z" />
        </svg>

      </div>
      <button class="btn btn-primary" @click.prevent="validation">{{ loading }}
        <div v-if="openL">
          <span class="spinner-border spinner-border-sm gap-2" aria-hidden="true" style="margin-right: 5px;"></span>
          <span role="status">
            <small style="vertical-align: inherit;">
              <small style="vertical-align: inherit;">Cargando...</small>
            </small>
          </span>
        </div>
      </button>
      <div class="alert alert-danger d-flex align-items-center" role="alert" style="position: absolute; top: 75%;"
        v-if="openA">
        <svg xmlns="http://www.w3.org/2000/svg" class="bi bi-exclamation-triangle-fill flex-shrink-0 me-2"
          viewBox="0 0 16 16" width="16" height="16" aria-label="Danger">
          <path
            d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z" />
        </svg>
        <div>
          El usuario o contraseña son incorrectos!
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import LoginService from '@/services/LoginService';
import { useRouter } from 'vue-router';
import { userGlobalStore } from '@/store/userGlobal';

let gUser = userGlobalStore()

const username = ref<string>('');
const password = ref<string>('');
let loading = ref('Acceso')
const router = useRouter();
const openA = ref(false)
const openL = ref(false)

const validation = async (): Promise<void> => {
  try {
    loading.value = '';
    openL.value = !openL.value

    const credential = new LoginService();
    // Espera a que la solicitud se complete y actualice la variable 'user'
    await credential.fetchByLogin(username.value, password.value);

    // Obtén el usuario después de que la solicitud se complete
    const user = credential.getMs();

    console.log(user.value)
    // Validación
    if (!!user.value && user.value.message === 'Autenticacion exitosa') {
      router.push('/PrinPage');
      gUser.setUser(user.value.nombre_usuario)
      console.log('Credenciales válidas');
    } else {
      openL.value = !openL.value
      loading.value = 'Acceso'
      if (openA.value == false) {
        openA.value = !openA.value
      }

    }
  } catch (error) {
    console.error('Error al realizar la validación:', error);
  }
};

onMounted(() => {
  //por si quiero poner algo antes cuando se monta la pagina
});

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

#app2 {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.form {
  position: relative;
  width: 400px;
  height: 450px;
  background: transparent;
  box-shadow: 0 0 5px gray, 0 0 25px gray, 0 0 50px gray, 0 0 200px gray;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
  backdrop-filter: blur(10px);
  color: black;
  font-family: 'Poppins', sans-serif;

  @media screen and (max-width: 600px) {
    width: 320px;
  }
}

.inputbox {
  display: flex;
  align-items: center;
  width: 80%;
}

.inputbox input {
  width: 100%;
  height: 50px;
  background: transparent;
  margin-bottom: 2em;
  padding: 1em 0 0 0.5em;
  border: none;
  border-bottom: 1px solid black;
  font-size: small;
  outline: none;
  color: black;
  padding-right: 20px;
}

.inputbox svg {
  transform: translateY(-50%) translateX(-90%);
  fill: black
    /*para cambiar el color del contenido */
}

.inputbox label {
  position: absolute;
  left: 12%;
  transform: translateY(-50%);
  transition: transform 200ms;
  pointer-events: none
    /* evita q el label interfiera en el input*/
  ;
}

input:focus+label,
input:valid+label {
  transform: translate(0, -30px) scale(0.8);
}

h2 {
  position: absolute;
  text-align: center;
  top: 14%;
  text-shadow: 0 0 5px white;
}

h4 {
  position: absolute;
  top: 5%;
  left: 5%;
  color: darkblue;
}

button {
  width: 80%;
  min-width: 250px;
  border-radius: 10px;
  background-color: darkblue;
  box-shadow: 0 1em 4em rgba(212, 234, 255, 0.2);
  border: none;
  color: white;
  margin-bottom: 10px;
}

.alert {
  @media screen and (max-width: 600px) {
    width: 95%;
  }
}
</style>