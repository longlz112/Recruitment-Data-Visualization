import {createRouter,createWebHistory} from "vue-router";

import Home from '@/views/home.vue'
import Login from "@/views/login.vue";
import Charts from "@/views/charts.vue";


const router = createRouter({
    history:createWebHistory(),
    routes:[
        {
            path:'/',
            name:'home',
            title:'首页',
            component:Home
        },
        {
            path:'/login',
            name:'Login',
            title:'登录',
            component:Login
        },
        {
            path:'/charts',
            name:'Charts',
            title:'图表',
            component:Charts
        }

    ]
})
export default router