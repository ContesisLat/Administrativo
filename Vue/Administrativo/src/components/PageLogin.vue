<template>
    <div class="login-wrapper">
        <div class="login-card fade-slide">

            <!-- LEFT -->
            <aside class="login-left">
                <div class="brand">
                    <!-- aquí puedes poner tu logo -->
                    <img src="@/assets/LogoCorto.png" class="brand-logo" />
                </div>

                <div class="left-text">
                    <small>Bienvenido a</small>
                    <h2>
                        Estrategia 3.0<br />
                        Su ERP empresarial
                    </h2>
                </div>
            </aside>

            <!-- RIGHT -->
            <section class="login-right">
                <h1>Iniciar Sesion</h1>
                <p class="subtitle">
                    Acceda a sus Modulos ERP de manera rapida y segura.
                </p>

                <form @submit.prevent="validation" class="form">

                    <!-- Usuario -->
                    <div class="field">
                        <input id="user" type="text" v-model="username" required :class="{ error: openA }" />
                        <label for="user">Usuario</label>
                        <i class="bi bi-person"></i>
                    </div>

                    <!-- Password -->
                    <div class="field">
                        <input :type="showPassword ? 'text' : 'password'" id="password" v-model="password" required
                            :class="{ error: openA }" />
                        <label for="password">Password</label>
                        <i class="bi" :class="showPassword ? 'bi-eye-slash' : 'bi-eye'"
                            @click="showPassword = !showPassword"></i>
                    </div>

                    <!-- Button -->
                    <button class="btn-primary" type="submit" :disabled="openL">
                        <span v-if="!openL">{{ loading }}</span>
                        <span v-else class="loading">
                            <span class="spinner-border spinner-border-sm"></span>
                            Cargando...
                        </span>
                    </button>

                    <!-- Error -->
                    <transition name="fade">
                        <div v-if="openA" class="error-box">
                            <i class="bi bi-exclamation-triangle-fill"></i>
                            Usuario o contraseña incorrectos
                        </div>
                    </transition>

                </form>
            </section>
        </div>
    </div>
</template>


<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import LoginService from '@/services/LoginService';
import { useRouter } from 'vue-router';
import { userGlobalStore } from '@/store/userGlobal';

let gUser = userGlobalStore()

const username = ref('');
const password = ref('');
const loading = ref('Acceso');

const openA = ref(false);
const openL = ref(false);
const showPassword = ref(false);

const router = useRouter();

const validation = async (): Promise<void> => {
    try {
        openA.value = false;
        openL.value = true;
        loading.value = '';

        const credential = new LoginService();
        await credential.fetchByLogin(username.value, password.value);

        const user = credential.getMs();

        if (user.value && user.value.message === 'Autenticacion exitosa') {
            router.push('/PrinPage');
            gUser.setUser(user.value.nombre_usuario)

        } else {
            throw new Error('Credenciales inválidas');
        }
    } catch (error) {
        openA.value = true;
    } finally {
        openL.value = false;
        loading.value = 'Acceso';
    }
};

</script>

<style scoped>
/* WRAPPER */
.login-wrapper {
    min-height: 100vh;
    background: #f2f4fa;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* CARD */
.login-card {
    width: 780px;
    max-width: 92%;
    min-height: 480px;
    background: #ffffff;
    border-radius: 18px;
    display: flex;
    overflow: hidden;

    /* sombra tipo referencia */
    box-shadow:
        0 20px 40px rgba(0, 0, 0, 0.08),
        0 10px 20px rgba(95, 108, 255, 0.15);
}

.login-card {
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.login-card:hover {
    transform: translateY(-6px);
    box-shadow:
        0 30px 60px rgba(0, 0, 0, 0.12),
        0 15px 30px rgba(95, 108, 255, 0.25);
}

.brand {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 15px;
    z-index: 1;
}

.brand-logo {
    width: 250px;
    height: auto;
}

/* LEFT PANEL */
.login-left {
    position: relative;
    flex: 1;
    padding: 40px;
    color: #fff;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    margin: 10px;

    background: linear-gradient(120deg,
            #6a73ff,
            #8f9bff,
            #b8c1ff,
            #6a73ff);
    background-size: 300% 300%;
    animation: gradientMove 12s ease infinite;
}

@keyframes gradientMove {
    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}


/* efecto blur/glass como referencia */
.login-left::before {
    content: "";
    position: absolute;
    inset: -20%;
    background:
        radial-gradient(circle at top left,
            rgba(255, 255, 255, 0.45),
            transparent 60%),
        radial-gradient(circle at bottom right,
            rgba(255, 255, 255, 0.25),
            transparent 55%);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    opacity: 0.9;
    pointer-events: none;
    /* no bloquea clicks */
    z-index: 0;
}


/* contenido por encima del blur */
.login-left * {
    position: relative;
    z-index: 1;
}

.left-text small {
    opacity: 0.9;
}

.left-text h2 {
    font-weight: 600;
    line-height: 1.35;
}

/* RIGHT PANEL */
.login-right {
    flex: 1;
    padding: 40px 36px;
    /* menos padding */
}

.login-right h1 {
    font-size: 22px;
    font-weight: 700;
}

.subtitle {
    font-size: 13px;
    color: #6c757d;
    margin-bottom: 26px;
}

/* FORM */
.field {
    position: relative;
    margin-bottom: 22px;
}

.field input {
    width: 100%;
    padding: 13px 38px 13px 12px;
    border-radius: 10px;
    border: 1px solid #e0e0e0;
    outline: none;
    font-size: 14px;
    transition: 0.25s;
}

.field input:focus {
    border-color: #6a73ff;
    box-shadow: 0 0 0 3px rgba(106, 115, 255, 0.15);
}

.field label {
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: #999;
    font-size: 13px;
    pointer-events: none;
    transition: 0.25s;
    background: #fff;
}

.field input:focus+label,
.field input:not(:placeholder-shown)+label {
    top: -7px;
    font-size: 11px;
    padding: 0 6px;
    color: #6a73ff;
}

.field input.error {
    border-color: #dc3545;
    box-shadow: 0 0 0 2px rgba(220, 53, 69, 0.2);
}

/* también el label cambia de color si hay error */
.field input.error+label {
    color: #dc3545;
}


.field i {
    position: absolute;
    right: 12px;
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
    color: #777;
}

/* BUTTON */
.btn-primary {
    width: 100%;
    padding: 13px;
    border-radius: 12px;
    border: none;
    background: #6a73ff;
    color: #fff;
    font-weight: 600;
    transition: 0.25s;
}

.btn-primary:hover:not(:disabled) {
    background: #5560e6;
}

.btn-primary:disabled {
    opacity: 0.7;
}

/* ERROR */
.error-box {
    margin-top: 14px;
    color: #dc3545;
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
}

/* ANIMATION */
.fade-slide {
    animation: fadeSlide 0.5s ease;
}

@keyframes fadeSlide {
    from {
        opacity: 0;
        transform: translateY(16px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .login-card {
        flex-direction: column;
    }

    .login-left {
        min-height: 180px;
    }
}
</style>