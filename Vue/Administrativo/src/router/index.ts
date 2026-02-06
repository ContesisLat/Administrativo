import { createRouter,createWebHistory,RouteRecordRaw } from "vue-router";
import PageLogin from '@/components/PageLogin.vue';
import PrinPage from '@/components/PrinPage.vue';

const routes:Array<RouteRecordRaw> = [
    {
        path: "/",
        redirect: to => {return{name:'PageLogin'}}
    },
    {
        path:'/PageLogin',
        name:'PageLogin',
        component:PageLogin
    },
    {
        path:'/PrinPage',
        name:'PrinPage',
        component: PrinPage,
    },
      

]
const router = createRouter({
    history:createWebHistory(process.env.BASE_URL),
    routes
})

export default router